import hashlib
from typing import Dict, List
class AreaColorMapper:
    def __init__(self):
        self._color_map: Dict[str, str] = {}
    def _hash_string_to_color(self, input_str: str) -> str:
        h = hashlib.md5(input_str.encode()).hexdigest()[:6]
        if len(h) == 0:
            return "unknown"
        color_map = {
            'a': '#FF0000',      
            'b': '#00FF00',        
            'c': '#0000FF',       
            'd': '#FFFF00',         
            'e': '#00FFFF',       
            'f': '#FF00FF',          
        }
        first_char = h[0] if h else '?'
        return color_map.get(first_char, '#FFFFFF')
    def map_areas(self) -> Dict[str, str]:
        self._color_map.clear()
        sample_inputs: List[tuple] = [
            ("north_region", "standard"),
            ("south_islands", "special"),
            ("eastern_forest", "dynamic"),
            ("western_desert", "legacy"),
            ("central_city", "modern")
        ]
        for input_str, rule in sample_inputs:
            color = self._hash_string_to_color(input_str)
            self._color_map[input_str] = color
        return self._color_map
if __name__ == '__main__':
    mapper = AreaColorMapper()
    result = mapper.map_areas()
    for area, color in sorted(result.items()):
        print(f"{area}: {color}")