class RegionMapper:
    def __init__(self):
        self._colors = {
            "north": "#001F3F",
            "south": "#C71585",
            "east": "#FFD92F",
            "west": "#6A4EAF"
        }
    def map_regions(self, region_names: list) -> list:
        return [(name, self._colors[name]) for name in region_names if name in self._colors]
if __name__ == '__main__':
    regions = ["north", "south", "east"]
    mapper = RegionMapper()
    result = mapper.map_regions(regions)
    print(result)