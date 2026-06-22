UNIT_FACTOR = 1000

def _validate_distance(value: float) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError("Distance must be a number")
    if value < 0:
        raise ValueError("Distance cannot be negative")
    return float(value)

class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        validated_value = _validate_distance(kilometers)
        return validated_value * UNIT_FACTOR

if __name__ == '__main__':
    converter_instance = UnitConverter()
    print(converter_instance.kilometers_to_meters(1.0))
    print(converter_instance.kilometers_to_meters(100.25))