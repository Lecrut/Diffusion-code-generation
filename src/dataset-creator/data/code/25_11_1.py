class RegionMapper:
    def __init__(self):
        self.regions = []
    def add_region(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Region names must be strings.")
        hash_val = sum(ord(c) * (i + 1) for i, c in enumerate(name)) % 256
        r = ((hash_val >> 0) & 0xFF)
        g = ((hash_val >> 8) & 0xFF)
        b = ((hash_val >> 16) & 0xFF)
        self.regions.append((name, f"#{r:02X}{g:02X}{b:02X}"))
    def get_region_colors(self):
        return self.regions
if __name__ == '__main__':
    mapper = RegionMapper()
    sample_regions = ["North", "South", "East", "West"]
    for name in sample_regions:
        mapper.add_region(name)
    result = mapper.get_region_colors()
    print(result)