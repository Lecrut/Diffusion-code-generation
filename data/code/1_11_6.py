class WeightManager:
    def __init__(self):
        self.weights = {}

    def store(self, date, weight):
        self.weights[date] = weight

    def retrieve(self, date):
        return self.weights.get(date)

    def update(self, date, weight):
        if date in self.weights:
            self.weights[date] = weight
            return True
        return False

    def get_all(self):
        return self.weights.copy()

    def delete(self, date):
        if date in self.weights:
            del self.weights[date]
            return True
        return False

if __name__ == '__main__':
    manager = WeightManager()
    manager.store('2023-01-01', 70.5)
    manager.store('2023-01-02', 71.0)
    manager.store('2023-01-03', 70.8)

    print(manager.retrieve('2023-01-01'))
    print(manager.retrieve('2023-01-02'))

    manager.update('2023-01-02', 71.5)
    print(manager.retrieve('2023-01-02'))

    print(manager.get_all())

    manager.delete('2023-01-03')
    print(manager.get_all())

    print(manager.retrieve('2023-01-03'))