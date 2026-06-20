class WeightManager:
    def __init__(self):
        self._data = {}

    def store(self, user_id, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number")
        self._data[user_id] = weight
        return self._data[user_id]

    def retrieve(self, user_id):
        return self._data.get(user_id)

    def update(self, user_id, new_weight):
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Weight must be a positive number")
        if user_id not in self._data:
            raise KeyError("User ID not found")
        self._data[user_id] = new_weight
        return self._data[user_id]

if __name__ == '__main__':
    manager = WeightManager()
    initial_store = manager.store("user_001", 70.5)
    retrieve_val = manager.retrieve("user_001")
    update_val = manager.update("user_001", 71.2)
    non_existent = manager.retrieve("user_099")
    print(initial_store)
    print(retrieve_val)
    print(update_val)
    print(non_existent)