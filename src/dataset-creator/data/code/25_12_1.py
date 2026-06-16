import re
from typing import Dict, List, Tuple
class AreaColorMapper:
    def __init__(self):
        self._color_map: Dict[str, str] = {}
    def _normalize_area(self, area_str: str) -> str:
        return area_str.strip().lower()
    def _generate_color_id(self, normalized_area: str) -> Tuple[int, int]:
        hash_val = sum(ord(c) for c in normalized_area) % 256
        r = (hash_val * 3 + 128) & 0xFF
        g = ((hash_val * 7) ^ 42) & 0xFF
        b = ((hash_val // 17) << 4) | ((hash_val % 17)) & 0x0F
        return r, g, b
    def _get_or_generate_color(self, normalized_area: str) -> Tuple[int, int]:
        if normalized_area not in self._color_map:
            color = self._generate_color_id(normalized_area)
            self._color_map[normalized_area] = color
        return self._color_map[normalized_area]
    def map_areas(self, input_strings: List[str]) -> Dict[str, str]:
        result: Dict[str, str] = {}
        for area in input_strings:
            norm_area = self._normalize_area(area)
            r, g, b = self._get_or_generate_color(norm_area)
            color_hex = f"#{r:02X}{g:02X}{b:02X}"
            result[norm_area] = color_hex
        return result
if __name__ == '__main__':
    mapper = AreaColorMapper()
    sample_inputs = [
        "north_region",
        "south_zone1",
        "east_territory",
        "west_district_alpha",
        "central_hub"
    ]
    output_map = mapper.map_areas(sample_inputs)
    for area, color in sorted(output_map.items()):
        print(f"{area}: {color}")