class WeightManager:
    def __init__(self):
        self._data = {}

    def store(self, entry_id, weight_value):
        self._data[entry_id] = weight_value

    def retrieve(self, entry_id):
        return self._data.get(entry_id)

    def update(self, entry_id, new_weight):
        if entry_id in self._data:
            self._data[entry_id] = new_weight
            return True
        return False

    def get_all(self):
        return dict(self._data)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store("user_001", 75.5)
    manager.store("user_002", 68.2)
    initial_value = manager.retrieve("user_001")
    manager.update("user_001", 76.0)
    updated_value = manager.retrieve("user_001")
    print(initial_value)
    print(updated_value)
    print(manager.get_all())