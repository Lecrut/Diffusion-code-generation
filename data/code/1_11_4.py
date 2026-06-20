class WeightManager:
    def __init__(self):
        self._records = {}
        self._sorted_keys = []
    def store_weight(self, date, weight):
        if date not in self._records:
            self._sorted_keys.append(date)
            self._sorted_keys.sort()
        self._records[date] = float(weight)
    def retrieve_weight(self, date):
        return self._records.get(date)
    def update_weight(self, date, weight):
        if date in self._records:
            self._records[date] = float(weight)
            return True
        return False
    def get_recent(self, count):
        if count <= 0:
            return {}
        recent_dates = self._sorted_keys[-count:]
        return {d: self._records[d] for d in recent_dates}
    def get_statistics(self):
        if not self._records:
            return None
        values = list(self._records.values())
        return {
            "min": min(values),
            "max": max(values),
            "average": sum(values) / len(values),
            "count": len(values)
        }

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 75.0)
    manager.store_weight("2023-10-05", 74.5)
    manager.store_weight("2023-10-10", 73.2)
    manager.store_weight("2023-10-15", 72.8)
    manager.update_weight("2023-10-05", 74.8)
    print(manager.retrieve_weight("2023-10-05"))
    print(manager.get_recent(2))
    print(manager.get_statistics())