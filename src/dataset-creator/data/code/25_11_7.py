class RegionMapper:
    def __init__(self):
        self.regions = []
    def add_region(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Region names must be strings.")
        hash_val = sum(ord(c) * (i + 1) % 256 for i, c in enumerate(name))
        r = int(hash_val / 3.0) & 0xFF
        g = int((hash_val - r) / 7.0) & 0xFF
        b = int((hash_val * 4 + hash_val % 156) / 255) & 0xFF
        self.regions.append({
            'name': name,
            'color': f"#{r:02X}{g:02X}{b:02X}"
        })
    def get_region_colors(self):
        return [(region['name'], region['color']) for region in self.regions]
if __name__ == '__main__':
    mapper = RegionMapper()
    sample_regions = [
        "North", 
        "South", 
        "East", 
        "West"
    ]
    for name in sample_regions:
        mapper.add_region(name)
    result = mapper.get_region_colors()
    print(result)