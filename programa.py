import geopandas as gpd

#Un geodataframe es una tabla de datos donde al menos una de sus columnas 
# contienen datos espaciales vectoriales (geometricos) puntos, lineas
# y poligonos

# Leer archivos que tengan datos espaciales
# Por ejemplo: Geojson

archivo = gpd.read_file("custom.geo.json")
