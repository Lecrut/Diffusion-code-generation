class WeightManager:
    def __init__(self):
        self._recordings = {}
        self._sorted_dates = []

    def _validate_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a numeric value")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        return float(weight)

    def store_weight(self, date, weight):
        if date in self._recordings:
            return False
        value = self._validate_weight(weight)
        self._recordings[date] = value
        self._insert_sorted_date(date)
        return True

    def _insert_sorted_date(self, date):
        dates = self._sorted_dates
        left, right = 0, len(dates)
        while left < right:
            mid = (left + right) // 2
            if dates[mid] < date:
                left = mid + 1
            else:
                right = mid
        dates.insert(left, date)

    def retrieve_weight(self, date):
        return self._recordings.get(date)

    def update_weight(self, date, weight):
        if date not in self._recordings:
            return False
        value = self._validate_weight(weight)
        self._recordings[date] = value
        return True

    def get_historical_weight(self, date):
        return self.retrieve_weight(date)

    def get_latest_weight(self):
        if not self._sorted_dates:
            return None
        latest_date = self._sorted_dates[-1]
        return self._recordings[latest_date]

    def remove_entry(self, date):
        if date not in self._recordings:
            return False
        del self._recordings[date]
        self._sorted_dates.remove(date)
        return True

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-05-01", 80.0)
    manager.store_weight("2023-05-05", 79.5)
    manager.store_weight("2023-05-02", 80.2)
    manager.update_weight("2023-05-02", 79.8)
    print(manager.get_latest_weight())
    print(manager.retrieve_weight("2023-05-05"))
    print(manager.remove_entry("2023-05-01"))
    print(manager.get_latest_weight())