import threading

class SingletonMap:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._map = {}
        return cls._instance

    def set_value(self, key, value):
        with self._lock:
            self._map[key] = value

    def get_value(self, key):
        with self._lock:
            return self._map.get(key)

if __name__ == '__main__':
    singleton_map = SingletonMap()
    singleton_map.set_value("pi", 3.14159)
    print(singleton_map.get_value("pi"))