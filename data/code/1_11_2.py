class WeightManager:
    _DEFAULT_CAPACITY = 100

    def __init__(self):
        self._entries = {}
        self._latest_date = None
        self._latest_weight = None

    def store_weight(self, date, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        if date in self._entries:
            return False
        self._entries[date] = weight
        if self._latest_date is None or date > self._latest_date:
            self._latest_date = date
            self._latest_weight = weight
        return True

    def retrieve_weight(self, date):
        return self._entries.get(date)

    def update_weight(self, date, weight):
        if date not in self._entries:
            return False
        self._entries[date] = weight
        if date == self._latest_date:
            self._latest_weight = weight
        elif self._latest_date is None or date > self._latest_date:
            self._latest_date = date
            self._latest_weight = weight
        return True

    def get_latest_weight(self):
        return self._latest_weight if self._latest_date is not None else None

    def get_recent_weights(self, limit=5):
        sorted_dates = sorted(self._entries.keys(), reverse=True)
        return {d: self._entries[d] for d in sorted_dates[:limit]}

    def remove_weight(self, date):
        if date not in self._entries:
            return False
        del self._entries[date]
        if self._latest_date == date:
            if self._entries:
                new_latest = sorted(self._entries.keys(), reverse=True)[0]
                self._latest_date = new_latest
                self._latest_weight = self._entries[new_latest]
            else:
                self._latest_date = None
                self._latest_weight = None
        return True

    def count_entries(self):
        return len(self._entries)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 80.0)
    manager.store_weight("2023-10-02", 79.5)
    manager.store_weight("2023-10-03", 79.0)
    manager.store_weight("2023-10-05", 78.5)
    manager.update_weight("2023-10-03", 78.8)
    manager.store_weight("2023-10-04", 79.2)
    print(manager.get_latest_weight())
    print(manager.get_recent_weights(3))
    print(manager.remove_weight("2023-10-01"))
    print(manager.count_entries())