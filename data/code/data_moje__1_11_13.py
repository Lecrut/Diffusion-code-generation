class WeightManager:
    def __init__(self):
        self._measurements = {}

    def store(self, date, weight):
        self._measurements[date] = weight

    def retrieve(self, date):
        return self._measurements.get(date)

    def update(self, date, weight):
        self.store(date, weight)

    def get_all(self):
        return dict(self._measurements)

    def remove(self, date):
        if date in self._measurements:
            del self._measurements[date]
            return True
        return False

    def get_average(self):
        if not self._measurements:
            return 0.0
        total = sum(self._measurements.values())
        count = len(self._measurements)
        return total / count

if __name__ == '__main__':
    manager = WeightManager()

    manager.store('2023-01-01', 70.5)
    manager.store('2023-02-01', 71.2)
    manager.store('2023-03-01', 70.8)

    print(manager.retrieve('2023-01-01'))
    print(manager.retrieve('2023-02-01'))
    print(manager.retrieve('2023-04-01'))

    manager.update('2023-01-01', 69.9)
    print(manager.retrieve('2023-01-01'))

    print(manager.get_all())
    print(manager.get_average())

    manager.remove('2023-02-01')
    print(manager.get_all())
    print(manager.get_average())