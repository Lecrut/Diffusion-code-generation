import threading
class ColorMapper:
    def __init__(self):
        self._color_map = {}
        self._lock = threading.Lock()
    def set_mapping(self, color_name, hex_code):
        with self._lock:
            self._color_map[color_name] = hex_code
    def get_mapping(self, color_name):
        with self._lock:
            return self._color_map.get(color_name)
if __name__ == '__main__':
    mapper = ColorMapper()
    sample_data = [
        ("Red", "#FF0000"),
        ("Green", "#00FF00"),
        ("Blue", "#0000FF"),
        ("Yellow", "#FFFF00")
    ]
    for name, hex_code in sample_data:
        mapper.set_mapping(name, hex_code)
    print(f"Mapping for Red: {mapper.get_mapping('Red')}")
    print(f"Mapping for Green: {mapper.get_mapping('Green')}")
    print(f"Mapping for Purple: {mapper.get_mapping('Purple')}")