import math

def convert_cubic_meters_to_liters(value: float) -> float:
    return value * 1000.0

def convert_liters_to_cubic_meters(value: float) -> float:
    return value / 1000.0

def convert_liters_to_milliliters(value: float) -> float:
    return value * 1000.0

def convert_milliliters_to_liters(value: float) -> float:
    return value / 1000.0

def convert_liters_to_gallons(value: float) -> float:
    return value / 3.785411784

def convert_gallons_to_liters(value: float) -> float:
    return value * 3.785411784

if __name__ == '__main__':
    result1 = convert_cubic_meters_to_liters(2.5)
    print(result1)
    result2 = convert_liters_to_gallons(5.0)
    print(result2)
    result3 = convert_gallons_to_liters(1.0)
    print(result3)
    result4 = convert_liters_to_milliliters(0.5)
    print(result4)