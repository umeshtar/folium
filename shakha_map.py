import json

import folium
from folium.plugins import Fullscreen

m = folium.Map(
    location=[22, 78],
    zoom_start=5
)

state_map_group = folium.FeatureGroup(name='State Maps').add_to(m)
city_map_group = folium.FeatureGroup(name='City Maps', show=False).add_to(m)
vistar_map_group = folium.FeatureGroup(name='Vistar Maps', show=False).add_to(m)
nagar_map_group = folium.FeatureGroup(name='Nagar Maps', show=False).add_to(m)

country_markers_group = folium.FeatureGroup('Country Markers').add_to(m)
state_marker_group = folium.FeatureGroup(name='State Markers', show=True).add_to(m)
city_marker_group = folium.FeatureGroup(name='City Markers', show=False).add_to(m)
vistar_marker_group = folium.FeatureGroup(name='Vistar Markers', show=False).add_to(m)
nagar_marker_group = folium.FeatureGroup(name='Nagar Markers', show=False).add_to(m)

country_icon = dict(color='pink')
state_icon = dict(color='green')
city_icon = dict(color='orange')
vistar_icon = dict(color='red')
nagar_icon = dict(color='blue')

f = open('state_area.geojson', 'r')
geo_json_data = json.load(f)
f.close()
folium.GeoJson(
    geo_json_data,
    name='Prant Map',
    zoom_on_click=True,
    style_function=lambda x: {
        "fillColor": "red",
    },
).add_to(state_map_group)

f = open('gujrat_mahanagars.geojson', 'r')
gujarat_geo_json_data = json.load(f)
f.close()

folium.GeoJson(
    gujarat_geo_json_data,
    name='Gujarat Map',
    zoom_on_click=True,
    style_function=lambda x: {
        "fillColor": "blue",
    },
).add_to(city_map_group)

f = open('vadodara_vistar.geojson', 'r')
vadodara_geo_json_data = json.load(f)
f.close()

folium.GeoJson(
    vadodara_geo_json_data,
    name='Vadodara Map',
    zoom_on_click=True,
    style_function=lambda x: {
        "fillColor": "green",
    },
).add_to(vistar_map_group)

f = open('sayaji_nagar.geojson', 'r')
sayaji_geo_json_data = json.load(f)
f.close()

folium.GeoJson(
    sayaji_geo_json_data,
    name='Sayaji Map',
    zoom_on_click=True,
    style_function=lambda x: {
        "fillColor": "orange",
    },
).add_to(nagar_map_group)

f = open('vishwamitri_nagar.geojson', 'r')
sayaji_geo_json_data = json.load(f)
f.close()

folium.GeoJson(
    sayaji_geo_json_data,
    name='Vishwamitri Map',
    zoom_on_click=True,
    style_function=lambda x: {
        "fillColor": "pink",
    },
).add_to(nagar_map_group)


folium.Marker(
    location=[22.3511, 78.6677],
    tooltip="Akhil Bharat",
    popup="""
        <h1>Akhil Bharat</h1>
        <p>3 Prant</p>
    """,
    icon=folium.Icon(**country_icon),
).add_to(country_markers_group)

folium.Marker(
    location=[23.0761, 71.7606],
    tooltip="Gujarat State",
    popup="""
        <h2>Name: Gujarat State<h2>
        <h3>Maha Nagar: 3 </h3>
    """,
    icon=folium.Icon(**state_icon),
).add_to(state_marker_group)

folium.Marker(
    location=[26.3313, 73.2527],
    tooltip="Rajasthan State",
    popup="""
        <h2>Name: Rajasthan State<h2>
        <h3>Maha Nagar: 7 </h3>
    """,
    icon=folium.Icon(**state_icon),
).add_to(state_marker_group)

folium.Marker(
    location=[19.1161, 75.8308],
    tooltip="Maharashtra State",
    popup="""
        <h2>Name: Maharashtra State<h2>
        <h3>Maha Nagar: 4 </h3>
    """,
    icon=folium.Icon(**state_icon),
).add_to(state_marker_group)

folium.Marker(
    location=[23.0, 72.6],
    tooltip="Ahmedabad Maha Nagar",
    popup="""
        <h2>Name: Ahmedabad Maha Nagar<h2>
        <h3>Vistar: 10 </h3>
    """,
    icon=folium.Icon(**city_icon),
).add_to(city_marker_group)

folium.Marker(
    location=[22.3, 73.2],
    tooltip="Vadodara Maha Nagar",
    popup="""
        <h2>Name: Vadodara Maha Nagar<h2>
        <h3>Vistar: 2 </h3>
    """,
    icon=folium.Icon(**city_icon),
).add_to(city_marker_group)

folium.Marker(
    location=[21.2, 72.8],
    tooltip="Surat Maha Nagar",
    popup="""
        <h2>Name: Surat Maha Nagar<h2>
        <h3>Vistar: 5 </h3>
    """,
    icon=folium.Icon(**city_icon),
).add_to(city_marker_group)

folium.Marker(
    location=[22.2572, 73.1866],
    tooltip="Vishwamitri Vistar",
    popup="""
        <h2>Name: Vishwamitri Vistar<h2>
        <h3>Nagar: 3 </h3>
    """,
    icon=folium.Icon(**vistar_icon),
).add_to(vistar_marker_group)

folium.Marker(
    location=[22.3036, 73.1845],
    tooltip="Sayaji Vistar",
    popup="""
        <h2>Name: Sayaji Vistar<h2>
        <h3>Nagar: 3 </h3>
    """,
    icon=folium.Icon(**vistar_icon),
).add_to(vistar_marker_group)

folium.Marker(
    location=[22.3125, 73.1756],
    tooltip="Alkapuri Nagar",
    popup="""
        <h2>Name: Alkapuri Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)

folium.Marker(
    location=[22.3096, 73.1959],
    tooltip="Sayaji Nagar",
    popup="""
        <h2>Name: Sayaji Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)

folium.Marker(
    location=[22.2941, 73.1878],
    tooltip="Navlakhi Nagar",
    popup="""
        <h2>Name: Navlakhi Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)

folium.Marker(
    location=[22.2713, 73.1889],
    tooltip="Manjalpur Nagar",
    popup="""
        <h2>Name: Manjalpur Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)

folium.Marker(
    location=[22.2524, 73.1860],
    tooltip="Makarpura Nagar",
    popup="""
        <h2>Name: Makarpura Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)

folium.Marker(
    location=[22.2358, 73.1827],
    tooltip="Maneja Nagar",
    popup="""
        <h2>Name: Maneja Nagar<h2>
        <h3>Sakha Sankhya: 15 </h3>
        <h3>Sakha Sikshak: Aarav Bhai </h3>
    """,
    icon=folium.Icon(**nagar_icon),
).add_to(nagar_marker_group)


# m.add_child(folium.LatLngPopup())
# folium.FitOverlays().add_to(m)
Fullscreen(
    position="topright",
    title="Expand me",
    title_cancel="Exit me",
    force_separate_button=True,
).add_to(m)
folium.LayerControl().add_to(m)
m.save("india_states_map.html")
