import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    _data = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def set_value(self, key: str, value: float) -> None:
        with self._lock:
            self._data[key] = value

    def get_value(self, key: str) -> float:
        with self._lock:
            return self._data.get(key, 0.0)

if __name__ == '__main__':
    singleton = Singleton()
    singleton.set_value('pi', 3.14159)
    print(singleton.get_value('pi'))