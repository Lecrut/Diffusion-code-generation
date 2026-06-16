class RegionMapper:
    def __init__(self):
        self._color_map = {
            "north": "#87CEEB",
            "south": "#2F4F4F",
            "east": "#FFD700",
            "west": "#B22222"
        }
    def map_regions(self, regions):
        return [(name, self._color_map[name]) for name in regions if name.lower() in self._color_map]
if __name__ == '__main__':
    mapper = RegionMapper()
    sample_data = ["north", "south", "east"]
    result = mapper.map_regions(sample_data)
    print(result)