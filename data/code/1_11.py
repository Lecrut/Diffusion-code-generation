class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, date, weight):
        self.weights[date] = weight

    def retrieve_weight(self, date):
        return self.weights.get(date)

    def update_weight(self, date, weight):
        if date in self.weights:
            self.weights[date] = weight
            return True
        return False

    def get_all_weights(self):
        return dict(self.weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-01-01", 70.5)
    manager.store_weight("2023-01-02", 71.0)
    print(manager.retrieve_weight("2023-01-01"))
    manager.update_weight("2023-01-01", 70.0)
    print(manager.retrieve_weight("2023-01-01"))
    print(manager.get_all_weights())