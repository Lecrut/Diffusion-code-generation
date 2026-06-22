class WeightManager:
    _VALID_KEY = "weight_data"
    _INVALID_KEY = "invalid_key"

    def __init__(self):
        self._storage = {}
        self._history = []

    def _validate_input(self, date, weight):
        if not isinstance(date, str) or not date:
            raise ValueError("Date must be a non-empty string")
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Weight must be a non-negative number")

    def store_weight(self, date, weight):
        self._validate_input(date, weight)
        if date not in self._storage:
            self._storage[date] = weight
            self._history.append(date)
            return True
        return False

    def retrieve_weight(self, date):
        if not isinstance(date, str):
            return None
        return self._storage.get(date)

    def update_weight(self, date, weight):
        self._validate_input(date, weight)
        if date in self._storage:
            self._storage[date] = weight
            return True
        return False

    def get_all_weights(self):
        return dict(self._storage)

    def get_recent_weights(self, count=5):
        if not self._history:
            return {}
        recent_dates = self._history[-count:]
        return {d: self._storage[d] for d in recent_dates}

    def remove_entry(self, date):
        if date in self._storage:
            del self._storage[date]
            self._history.remove(date)
            return True
        return False

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 150.5)
    manager.store_weight("2023-10-02", 151.2)
    manager.store_weight("2023-10-03", 150.0)
    manager.update_weight("2023-10-02", 151.0)
    result = manager.get_recent_weights(2)
    print(result)
    latest = manager.retrieve_weight("2023-10-03")
    print(latest)
    manager.remove_entry("2023-10-01")
    print(manager.get_all_weights())