import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls)
                cls._data = {}
        return cls._instance

    def set_value(self, key, value):
        with self._lock:
            self._data[key] = value

    def get_value(self, key):
        with self._lock:
            return self._data.get(key)

if __name__ == '__main__':
    singleton = Singleton()
    singleton.set_value('pi', 3.14159)
    print(singleton.get_value('pi'))