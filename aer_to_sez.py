# aer_to_sez.py
#
# Usage: python3 aer_to_sez.py azimuth elevation range
#   converts azimuth, elevation, range to SEZ coordinates

# Parameters:
#   azimuth: degrees
#   elevation: degrees
#   range: km

# Output:
#   SEZ coordinates in km
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import math # math module
import sys # argv

# initialize script arguments
azimuth = float('nan') # latitude in degrees
elevation = float('nan') # latitude in degrees
range = float('nan') # latitude in degrees

# parse script arguments
if len(sys.argv) == 4:
  azimuth   = float(sys.argv[1])
  elevation = float(sys.argv[2])
  range     = float(sys.argv[3])
else:
  print(\
    'Usage: '\
    'python3 aer_to_sez azimuth elevation range'\
  )
  exit()

### script below this line ###

# radians
azimuth_rad = azimuth*math.pi/180.0
elevation_rad = elevation*math.pi/180.0

# calculate
s_km = -1.0*range*math.cos(elevation_rad)*math.cos(azimuth_rad)
e_km = range*math.cos(elevation_rad)*math.sin(azimuth_rad)
z_km = range*math.sin(elevation_rad)

# print
print(s_km)
print(e_km)
print(z_km)