class RegionMapper:
    def __init__(self):
        self.regions = []
    def add_region(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Region names must be strings.")
        hex_color = f"#{int(hashlib.md5(name.encode()).hexdigest(), 16):06x}"
        self.regions.append((name, hex_color))
    def get_region_colors(self) -> list:
        return [region for region in self.regions]
import hashlib
if __name__ == '__main__':
    mapper = RegionMapper()
    sample_regions = ["North", "South", "East", "West"]
    for name in sample_regions:
        mapper.add_region(name)
    result = mapper.get_region_colors()
    print(result)