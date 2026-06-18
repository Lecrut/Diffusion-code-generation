from typing import List, Tuple
class RegionColorMapper:
    def __init__(self) -> None:
        self._color_map = {
            "North": "#FF99CC",
            "South": "#336699",
            "East": "#FFFF00",
            "West": "#FFFFFF"
        }
    def map_regions(self, region_names: List[str]) -> List[Tuple[str, str]]:
        return [(name, self._color_map.get(name, "#808080")) for name in region_names]
if __name__ == '__main__':
    mapper = RegionColorMapper()
    sample_regions = ["North", "South", "East"]
    result = mapper.map_regions(sample_regions)
    print(result)