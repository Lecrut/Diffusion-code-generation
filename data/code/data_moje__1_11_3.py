class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, date, weight):
        self.weights[date] = float(weight)

    def retrieve_weight(self, date):
        return self.weights.get(date)

    def update_weight(self, date, new_weight):
        if date in self.weights:
            self.weights[date] = float(new_weight)
            return True
        return False

    def get_all_weights(self):
        return dict(self.weights)

    def get_latest_weight(self):
        if not self.weights:
            return None
        latest_date = max(self.weights.keys())
        return self.weights[latest_date]

    def get_weight_history(self):
        sorted_dates = sorted(self.weights.keys())
        return [(date, self.weights[date]) for date in sorted_dates]

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 70.5)
    manager.store_weight("2023-10-02", 71.2)
    manager.store_weight("2023-10-03", 70.8)
    print(manager.retrieve_weight("2023-10-02"))
    manager.update_weight("2023-10-02", 71.5)
    print(manager.retrieve_weight("2023-10-02"))
    print(manager.get_latest_weight())
    print(manager.get_weight_history())