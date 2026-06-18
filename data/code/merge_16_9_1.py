import threading
class ColorMapper:
    def __init__(self):
        self._color_map = {}
        self._lock = threading.Lock()
    def load_data(self, data):
        with self._lock:
            self._color_map = data
    def get_color_name(self, hex_code):
        with self._lock:
            return self._color_map.get(hex_code)
if __name__ == '__main__':
    mapper = ColorMapper()
    sample_data = {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow"
    }
    mapper.load_data(sample_data)
    print(f"Color mapping for #FF0000: {mapper.get_color_name('#FF0000')}")
    print(f"Color mapping for #00FF00: {mapper.get_color_name('#00FF00')}")
    print(f"Color mapping for #123456: {mapper.get_color_name('#123456')}")