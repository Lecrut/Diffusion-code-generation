class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, key, weight):
        self._weights[key] = float(weight)

    def retrieve(self, key):
        if key in self._weights:
            return self._weights[key]
        raise KeyError(f"Key '{key}' not found")

    def update(self, key, new_weight):
        if key not in self._weights:
            raise KeyError(f"Key '{key}' not found, cannot update")
        self._weights[key] = float(new_weight)

    def get_all(self):
        return dict(self._weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.store("person_1", 70.5)
    wm.store("person_2", 85.0)
    wm.store("person_3", 62.3)

    print(wm.retrieve("person_1"))
    print(wm.retrieve("person_2"))

    wm.update("person_1", 72.0)
    print(wm.retrieve("person_1"))

    print(wm.get_all())