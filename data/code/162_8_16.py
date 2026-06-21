import threading

class SingletonMap:
    _instance = None
    _lock = threading.Lock()
    _map = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonMap, cls).__new__(cls)
        return cls._instance

    def set_value(self, key: str, value: float) -> None:
        with self._lock:
            self._map[key] = value

    def get_value(self, key: str) -> float:
        with self._lock:
            return self._map.get(key, 0.0)

if __name__ == '__main__':
    singleton_map = SingletonMap()
    singleton_map.set_value('a', 3.14)
    print(singleton_map.get_value('a'))