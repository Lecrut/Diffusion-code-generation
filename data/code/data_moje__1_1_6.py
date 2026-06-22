class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, date_str, weight_value):
        self._weights[date_str] = weight_value

    def retrieve_weight(self, date_str):
        return self._weights.get(date_str)

    def update_weight(self, date_str, weight_value):
        if date_str in self._weights:
            self._weights[date_str] = weight_value
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-01-01", 75.5)
    manager.store_weight("2023-01-02", 76.0)
    
    retrieved = manager.retrieve_weight("2023-01-01")
    print(f"Retrieved weight: {retrieved}")
    
    updated = manager.update_weight("2023-01-01", 75.0)
    print(f"Update successful: {updated}")
    
    all_weights = manager.get_all_weights()
    print(f"All weights: {all_weights}")