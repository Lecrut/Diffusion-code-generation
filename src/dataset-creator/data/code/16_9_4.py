import threading
class ColorNameManager:
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
    manager = ColorNameManager()
    print("Initial mapping for 'red':", manager.get_color_name("red"))
    print("Initial mapping for 'blue':", manager.get_color_name("blue"))
    manager.set_color_mapping("red", "Scarlet")
    manager.set_color_mapping("cyan", "Sky")
    print("Updated mapping for 'red':", manager.get_color_name("red"))
    print("Mapping for 'cyan' (new):", manager.get_color_name("cyan"))
    def worker(color, value):
        result = manager.get_color_name(color)
        print(f"Thread {threading.get_ident()} retrieved {color}: {result}")
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=("green", "Test"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Final mapping for 'red':", manager.get_color_name("red"))