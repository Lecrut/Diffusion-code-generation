class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, date_str, weight):
        self.weights[date_str] = weight

    def get_weight(self, date_str):
        if date_str in self.weights:
            return self.weights[date_str]
        return None

    def update_weight(self, date_str, new_weight):
        if date_str in self.weights:
            self.weights[date_str] = new_weight
            return True
        return False

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-01-01", 70.5)
    manager.store_weight("2023-01-02", 71.0)
    print(manager.get_weight("2023-01-01"))
    print(manager.update_weight("2023-01-01", 72.0))
    print(manager.get_weight("2023-01-01"))
    print(manager.get_weight("2023-01-05"))