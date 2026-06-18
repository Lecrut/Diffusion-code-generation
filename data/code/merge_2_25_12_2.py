import hashlib
from typing import Dict, List, Tuple
class AreaColorMapper:
    def __init__(self):
        self.standard_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF"]
        self.color_map: Dict[str, str] = {}
    def _hash_string(self, input_str: str) -> int:
        return sum(ord(c) for c in input_str.lower()) % len(self.standard_colors)
    def generate_mapping(self, area_names: List[str]) -> None:
        seen_hashes = set()
        for name in area_names:
            h_val = self._hash_string(name)
            if h_val not in seen_hashes:
                color_idx = h_val % len(self.standard_colors)
                new_color = self.standard_colors[color_idx]
                while new_color in [self.color_map.get(n, None) for n in area_names]:
                    color_idx += 1
                    new_color = self.standard_colors[color_idx % len(self.standard_colors)]
                final_hash = hash(name + str(color_idx))
                while (final_hash, new_color) in [(hash(n), c) for n, c in self.color_map.items()]:
                    color_idx += 1
                    new_color = self.standard_colors[color_idx % len(self.standard_colors)]
                self.color_map[name] = new_color
    def get_mapping_for_area(self, area_name: str) -> Tuple[str, str]:
        return (area_name, self.color_map.get(area_name, "#0000FF"))
if __name__ == '__main__':
    mapper = AreaColorMapper()
    sample_areas = [
        "north_region",
        "south_valley",
        "east_mountains",
        "west_coast",
        "central_plain"
    ]
    for area in sample_areas:
        mapper.generate_mapping([area])
    print("Generated Color Map:")
    for name, color in sorted(mapper.color_map.items()):
        print(f"{name}: {color}")