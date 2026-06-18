import threading
class ColorManager:
    def __init__(self):
        self._color_map = {
            "red": "Crimson",
            "blue": "Azure",
            "green": "Emerald",
            "yellow": "Gold",
            "white": "Ivory"
        }
        self._lock = threading.Lock()
    def get_color_name(self, color_key: str) -> str | None:
        with self._lock:
            return self._color_map.get(color_key)
    def set_color_mapping(self, color_key: str, color_name: str):
        with self._lock:
            self._color_map[color_key] = color_name
if __name__ == '__main__':
    manager = ColorManager()
    print("Initial mapping for red:", manager.get_color_name("red"))
    print("Initial mapping for blue:", manager.get_color_name("blue"))
    manager.set_color_mapping("red", "Scarlet")
    print("Updated mapping for red:", manager.get_color_name("red"))
    manager.set_color_mapping("green", "ForestGreen")
    print("Updated mapping for green:", manager.get_color_name("green"))
    print("Mapping for yellow:", manager.get_color_name("yellow"))
    print("Mapping for unknown color:", manager.get_color_name("purple"))