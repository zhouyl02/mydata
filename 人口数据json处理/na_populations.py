import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North American', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})

wm.render_to_file('na_populations.svg')
