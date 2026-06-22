class WeightManager:
    _INVALID_INPUT = "Invalid input type"
    _NOT_FOUND = "Date not found"

    def __init__(self):
        self._records = {}

    def _validate_weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(self._INVALID_INPUT)
        if value < 0:
            raise ValueError("Weight cannot be negative")
        return float(value)

    def store_weight(self, date_str, weight):
        if not isinstance(date_str, str):
            raise TypeError(self._INVALID_INPUT)
        if not date_str:
            raise ValueError("Date string cannot be empty")
        validated_weight = self._validate_weight(weight)
        self._records[date_str] = validated_weight
        return date_str

    def retrieve_weight(self, date_str):
        if not isinstance(date_str, str):
            raise TypeError(self._INVALID_INPUT)
        return self._records.get(date_str)

    def update_weight(self, date_str, new_weight):
        if not isinstance(date_str, str):
            raise TypeError(self._INVALID_INPUT)
        if date_str not in self._records:
            return False
        validated_weight = self._validate_weight(new_weight)
        self._records[date_str] = validated_weight
        return True

    def get_statistics(self):
        if not self._records:
            return None
        values = list(self._records.values())
        return {
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values),
            "count": len(values)
        }

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("2023-10-01", 75.5)
    manager.store_weight("2023-10-02", 76.0)
    manager.store_weight("2023-10-03", 74.5)
    result = manager.update_weight("2023-10-02", 75.0)
    print(result)
    stats = manager.get_statistics()
    print(stats["avg"])
    print(manager.retrieve_weight("2023-10-02"))