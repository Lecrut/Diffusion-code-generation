import hashlib
from typing import Dict, Set
class AreaColorMapper:
    def __init__(self):
        self.color_map: Dict[str, str] = {}
        self._initialize_colors()
    def _initialize_colors(self) -> None:
        predefined_areas = {
            "forest": "#2E8B57",
            "desert": "#F4A460",
            "mountain": "#808080",
            "ocean": "#1E90FF",
            "jungle": "#006400"
        }
        self.color_map.update(predefined_areas)
    def _hash_string_to_color(self, input_str: str) -> str:
        hash_obj = hashlib.md5(input_str.encode('utf-8'))
        hex_digest = hash_obj.hexdigest()[:6]
        r = int(hex_digest[0], 16)
        g = int(hex_digest[2], 16)
        b = int(hex_digest[4], 16)
        return f"#{r:02X}{g:02X}{b:02X}"
    def map_area_to_color(self, area_name: str) -> str:
        if area_name in self.color_map:
            return self.color_map[area_name]
        generated_color = self._hash_string_to_color(area_name.lower())
        self.color_map[area_name] = generated_color
        return generated_color
    def get_all_colors(self) -> Set[str]:
        return set(self.color_map.values())
if __name__ == '__main__':
    mapper = AreaColorMapper()
    test_areas = [
        "forest",
        "desert", 
        "mountain",
        "ocean",
        "jungle",
        "unknown_region_123",
        "another_place_xyz"
    ]
    results: Dict[str, str] = {}
    for area in test_areas:
        color = mapper.map_area_to_color(area)
        results[area] = color
    print("Area to Color Mapping:")
    for area, color in sorted(results.items()):
        print(f"{area}: {color}")
    all_colors_list = list(mapper.get_all_colors())
    print("\nTotal unique colors generated:", len(all_colors_list))