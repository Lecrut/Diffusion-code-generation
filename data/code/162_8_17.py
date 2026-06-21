import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
                    cls._data = {}
        return cls._instance

    def set_value(self, key, value):
        self._data[key] = value

    def get_value(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    singleton1 = Singleton()
    singleton2 = Singleton()
    singleton1.set_value('pi', 3.14159)
    print(singleton2.get_value('pi'))