class RegionMapper:
    def __init__(self):
        self._color_palette = {
            "Alps": "#FFFFFF",
            "Carpathians": "#8B4513",
            "Himalayas": "#2F4F4F",
            "Andes": "#696969"
        }
    def map_regions(self, region_names):
        result = []
        for name in region_names:
            if name in self._color_palette:
                color = self._color_palette[name]
            else:
                default_color = "#008000"
                result.append((name, default_color))
                continue
            result.append((name, color))
        return result
if __name__ == '__main__':
    mapper = RegionMapper()
    sample_regions = ["Alps", "Carpathians", "Himalayas"]
    output = mapper.map_regions(sample_regions)
    for region_name, hex_color in output:
        print(f"{region_name}: {hex_color}")