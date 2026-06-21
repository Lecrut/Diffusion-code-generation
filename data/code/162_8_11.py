import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
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
    print(singleton1 is singleton2)
    singleton1.set_value('key1', 3.14)
    print(singleton2.get_value('key1'))