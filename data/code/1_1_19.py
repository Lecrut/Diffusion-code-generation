class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, key, weight):
        self._weights[key] = weight

    def retrieve(self, key):
        return self._weights.get(key)

    def update(self, key, weight):
        if key in self._weights:
            self._weights[key] = weight
            return True
        return False

    def get_all(self):
        return dict(self._weights)

    def remove(self, key):
        if key in self._weights:
            del self._weights[key]
            return True
        return False

    def has_key(self, key):
        return key in self._weights

    def clear(self):
        self._weights.clear()

if __name__ == '__main__':
    wm = WeightManager()
    wm.store("user_1", 75.5)
    wm.store("user_2", 68.2)
    print("Stored user_1 weight:", wm.retrieve("user_1"))
    print("Stored user_2 weight:", wm.retrieve("user_2"))
    wm.update("user_1", 76.0)
    print("Updated user_1 weight:", wm.retrieve("user_1"))
    print("Non-existent user weight:", wm.retrieve("user_3"))
    print("All weights:", wm.get_all())
    print("Has user_1:", wm.has_key("user_1"))
    print("Has user_3:", wm.has_key("user_3"))
    print("Remove user_2:", wm.remove("user_2"))
    print("All weights after removal:", wm.get_all())
    wm.clear()
    print("All weights after clear:", wm.get_all())