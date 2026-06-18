import hashlib
from typing import Dict, List, Tuple
class AreaColorMapper:
    def __init__(self):
        self.color_palette = {
            'green': '#4CAF50',
            'blue': '#2196F3',
            'red': '#F44336',
            'yellow': '#FFEB3B',
            'purple': '#9C27B0'
        }
    def normalize_area(self, area: str) -> str:
        return ''.join(c.lower() for c in area if not c.isdigit())
    def get_color_for_area(self, area: str) -> Tuple[str, int]:
        normalized = self.normalize_area(area)
        if normalized in self.color_palette:
            return self.color_palette[normalized], len(normalized)
        hash_input = f"{normalized}_{len(area)}"
        hex_digest = hashlib.md5(hash_input.encode()).hexdigest()[:6]
        color_val = int(hex_digest, 16)
        return (f"#{hex_digest}", len(normalized))
def process_areas(areas: List[str]) -> Dict[str, str]:
    mapper = AreaColorMapper()
    result_map: Dict[str, str] = {}
    for area in areas:
        color_code, _ = mapper.get_color_for_area(area)
        result_map[area.upper()] = color_code
    return result_map
if __name__ == '__main__':
    sample_areas = [
        "central_park",
        "downtown_district_7",
        "north_hills",
        "west_coast_zone",
        "old_town_square"
    ]
    area_to_color_mapping = process_areas(sample_areas)
    for input_area, color in sorted(area_to_color_mapping.items()):
        print(f"{input_area}: {color}")