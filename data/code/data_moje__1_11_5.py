class WeightManager:
    STORAGE_KEY = "weight_data"
    ERROR_MISSING = "Date not found"
    
    def __init__(self):
        self._registry = {}
    
    def _validate_weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be numeric")
        if value < 0:
            raise ValueError("Weight cannot be negative")
        return float(value)
    
    def _validate_date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if len(date) == 0:
            raise ValueError("Date string cannot be empty")
        return date
    
    def store_weight(self, date, weight):
        validated_date = self._validate_date(date)
        validated_weight = self._validate_weight(weight)
        if validated_date in self._registry:
            return False
        self._registry[validated_date] = validated_weight
        return True
    
    def retrieve_weight(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if date in self._registry:
            return self._registry[date]
        return None
    
    def update_weight(self, date, weight):
        validated_date = self._validate_date(date)
        validated_weight = self._validate_weight(weight)
        if validated_date in self._registry:
            self._registry[validated_date] = validated_weight
            return True
        return False
    
    def get_weight_sum(self):
        if not self._registry:
            return 0.0
        return sum(self._registry.values())
    
    def get_average_weight(self):
        if not self._registry:
            return 0.0
        return self.get_weight_sum() / len(self._registry)
    
    def clear_all(self):
        self._registry.clear()
        return len(self._registry) == 0

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 150.5)
    manager.store_weight("2023-10-02", 151.2)
    manager.update_weight("2023-10-02", 150.8)
    retrieved = manager.retrieve_weight("2023-10-02")
    average = manager.get_average_weight()
    total = manager.get_weight_sum()
    print(retrieved)
    print(average)
    print(total)