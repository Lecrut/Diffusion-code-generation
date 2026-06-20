class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, entity_id, value, timestamp=None):
        if timestamp is None:
            import time
            timestamp = time.time()
        if entity_id not in self._weights:
            self._weights[entity_id] = []
        self._weights[entity_id].append((timestamp, value))

    def get_latest_weight(self, entity_id):
        if entity_id not in self._weights or not self._weights[entity_id]:
            return None
        return self._weights[entity_id][-1][1]

    def get_weight_history(self, entity_id):
        if entity_id not in self._weights:
            return []
        return [item[1] for item in self._weights[entity_id]]

    def update_weight(self, entity_id, value, timestamp=None):
        if timestamp is None:
            import time
            timestamp = time.time()
        if entity_id not in self._weights or not self._weights[entity_id]:
            self._weights[entity_id] = []
            self._weights[entity_id].append((timestamp, value))
        else:
            last_timestamp, last_value = self._weights[entity_id][-1]
            if timestamp < last_timestamp:
                raise ValueError("New timestamp cannot be earlier than the last recorded timestamp for this entity.")
            self._weights[entity_id].append((timestamp, value))

    def get_average_weight(self, entity_id):
        if entity_id not in self._weights or not self._weights[entity_id]:
            return None
        total = sum(item[1] for item in self._weights[entity_id])
        return total / len(self._weights[entity_id])

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("user_001", 70.5)
    manager.store_weight("user_001", 71.2)
    manager.store_weight("user_001", 70.8)
    manager.store_weight("user_002", 85.0)
    print(manager.get_latest_weight("user_001"))
    print(manager.get_weight_history("user_001"))
    print(manager.get_average_weight("user_001"))
    manager.update_weight("user_001", 71.5)
    print(manager.get_latest_weight("user_001"))
    print(manager.get_latest_weight("user_002"))
    print(manager.get_average_weight("user_002"))
    print(manager.get_weight_history("user_002"))