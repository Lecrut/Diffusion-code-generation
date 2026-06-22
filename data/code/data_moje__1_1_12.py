class WeightManager:
    def __init__(self):
        self.weights = {}

    def add_measurement(self, date, weight):
        self.weights[date] = float(weight)

    def get_measurement(self, date):
        return self.weights.get(date)

    def update_measurement(self, date, new_weight):
        if date in self.weights:
            self.weights[date] = float(new_weight)
            return True
        return False

    def get_all_measurements(self):
        return dict(self.weights)

    def get_average_weight(self):
        if not self.weights:
            return 0.0
        total = sum(self.weights.values())
        count = len(self.weights)
        return total / count

    def get_latest_weight(self):
        if not self.weights:
            return None
        latest_date = max(self.weights.keys())
        return self.weights[latest_date]

    def remove_measurement(self, date):
        if date in self.weights:
            del self.weights[date]
            return True
        return False

if __name__ == '__main__':
    manager = WeightManager()
    manager.add_measurement("2023-10-01", 75.5)
    manager.add_measurement("2023-10-08", 74.8)
    manager.add_measurement("2023-10-15", 75.0)
    
    print(manager.get_measurement("2023-10-01"))
    print(manager.get_all_measurements())
    print(manager.get_average_weight())
    print(manager.get_latest_weight())
    
    manager.update_measurement("2023-10-15", 74.5)
    print(manager.get_measurement("2023-10-15"))
    
    print(manager.remove_measurement("2023-10-08"))
    print(manager.get_all_measurements())
    print(manager.get_average_weight())