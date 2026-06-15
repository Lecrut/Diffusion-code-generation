import threading
class ColorManager:
    def __init__(self):
        self._color_map = {}
        self._lock = threading.Lock()
    def set_color_mapping(self, color_name, hex_code):
        with self._lock:
            self._color_map[color_name] = hex_code
    def get_color_mapping(self, color_name):
        with self._lock:
            return self._color_map.get(color_name)
    def get_all_mappings(self):
        with self._lock:
            return self._color_map.copy()
if __name__ == '__main__':
    manager = ColorManager()
    initial_data = {
        "Red": "#FF0000",
        "Green": "#00FF00",
        "Blue": "#0000FF"
    }
    for name, hex_code in initial_data.items():
        manager.set_color_mapping(name, hex_code)
    print("--- Initial Mappings ---")
    print(f"Red: {manager.get_color_mapping('Red')}")
    print(f"Green: {manager.get_color_mapping('Green')}")
    print(f"Yellow: {manager.get_color_mapping('Yellow')}")
    new_data = {
        "Yellow": "#FFFF00",
        "Cyan": "#00FFFF"
    }
    for name, hex_code in new_data.items():
        manager.set_color_mapping(name, hex_code)
    print("\n--- Updated Mappings ---")
    print(f"Red: {manager.get_color_mapping('Red')}")
    print(f"Green: {manager.get_color_mapping('Green')}")
    print(f"Yellow: {manager.get_color_mapping('Yellow')}")
    print(f"Cyan: {manager.get_color_mapping('Cyan')}")
    print("\n--- All Mappings ---")
    all_mappings = manager.get_all_mappings()
    for color, hex_code in all_mappings.items():
        print(f"{color}: {hex_code}")