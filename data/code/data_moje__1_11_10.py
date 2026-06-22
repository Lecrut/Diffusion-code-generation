class WeightManager:
    def __init__(self):
        self.weights = {}

    def store(self, date, weight):
        self.weights[date] = weight

    def retrieve(self, date):
        return self.weights.get(date)

    def update(self, date, new_weight):
        if date in self.weights:
            self.weights[date] = new_weight
        else:
            self.weights[date] = new_weight

    def get_all(self):
        return dict(self.weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store('2023-01-01', 70.5)
    manager.store('2023-01-02', 71.2)
    print(manager.retrieve('2023-01-01'))
    manager.update('2023-01-01', 70.0)
    print(manager.retrieve('2023-01-01'))
    print(manager.get_all())