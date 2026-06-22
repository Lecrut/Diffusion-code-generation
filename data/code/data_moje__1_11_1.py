class WeightManager:
    def __init__(self):
        self._data = {}

    def store(self, user_id, weight):
        self._data[user_id] = weight

    def retrieve(self, user_id):
        return self._data.get(user_id)

    def update(self, user_id, weight):
        if user_id in self._data:
            self._data[user_id] = weight
            return True
        return False

    def delete(self, user_id):
        if user_id in self._data:
            del self._data[user_id]
            return True
        return False

    def get_latest(self, user_id):
        return self._data.get(user_id)

    def get_all(self):
        return self._data.copy()

if __name__ == '__main__':
    manager = WeightManager()
    manager.store("user_101", 75.5)
    manager.store("user_102", 68.2)
    manager.update("user_101", 74.8)
    result = manager.retrieve("user_101")
    print(result)
    new_status = manager.update("user_103", 80.0)
    print(new_status)
    final_check = manager.get_latest("user_103")
    print(final_check)
    deleted = manager.delete("user_102")
    print(deleted)
    remaining = manager.get_all()
    print(remaining)