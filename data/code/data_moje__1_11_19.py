class WeightManager:
    def __init__(self):
        self._weights = {}

    def store(self, date, weight):
        self._weights[date] = float(weight)

    def retrieve(self, date):
        return self._weights.get(date)

    def update(self, date, weight):
        if date in self._weights:
            self._weights[date] = float(weight)
        else:
            raise KeyError(f"Date {date} does not exist. Use store() to add new entries.")

    def get_all(self):
        return dict(self._weights)

    def get_latest(self):
        if not self._weights:
            return None
        latest_date = max(self._weights, key=lambda k: k)
        return (latest_date, self._weights[latest_date])

    def get_average(self):
        if not self._weights:
            return None
        total = sum(self._weights.values())
        count = len(self._weights)
        return total / count

    def remove(self, date):
        if date in self._weights:
            return self._weights.pop(date)
        return None

if __name__ == '__main__':
    wm = WeightManager()

    wm.store('2023-01-01', 70.5)
    wm.store('2023-01-02', 71.0)
    wm.store('2023-01-03', 70.8)

    print(wm.retrieve('2023-01-01'))
    print(wm.get_all())
    print(wm.get_latest())
    print(wm.get_average())

    wm.update('2023-01-01', 70.2)
    print(wm.retrieve('2023-01-01'))
    print(wm.get_average())

    print(wm.remove('2023-01-02'))
    print(wm.get_all())
    print(wm.retrieve('2023-01-02'))