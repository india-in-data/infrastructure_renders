import geopandas
import sys

shp_f = sys.argv[1]
dest = sys.argv[2]

src = geopandas.read_file(shp_f)

src.to_file(dest, driver='GeoJSON')