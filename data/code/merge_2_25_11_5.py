class RegionColorMapper:
    def map_regions(self, region_names):
        color_palette = {
            "North": "#FF7F50",
            "South": "#2E8B57",
            "East": "#4169E1",
            "West": "#DC143C"
        }
        result = []
        for name in region_names:
            if name.upper() in color_palette:
                hex_value = color_palette[name.upper()]
                result.append((name, hex_value))
        return result
if __name__ == '__main__':
    regions = ["North", "South", "East"]
    mapper = RegionColorMapper()
    output = mapper.map_regions(regions)
    print(output)