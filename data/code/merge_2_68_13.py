from typing import Union
LITERS_PER_CUBIC_METER = 1000.0
GALLONS_US_PER_LITER = 0.264172052
KIROLITERS_PER_CUBIC_METER = 1.0
def cubic_meters_to_liters(value: float) -> float:
    return value * LITERS_PER_CUBIC_METER
def liters_to_cubic_meters(value: float) -> float:
    return value / LITERS_PER_CUBIC_METER
def kiloliters_to_liters(value: Union[float, int]) -> float:
    return value * KIROLITERS_PER_CUBIC_METER * 1000.0
def gallons_us_to_cubic_meters(value: Union[float, int]) -> float:
    return value / GALLONS_US_PER_LITER
if __name__ == '__main__':
    sample_values = {
        'cubic_meters_to_liters': 2.5,
        'liters_to_cubic_meters': 100,
        'kiloliters_to_liters': 3,
        'gallons_us_to_cubic_meters': 50
    }
    for func_name, input_val in sample_values.items():
        if func_name == 'cubic_meters_to_liters':
            result = cubic_meters_to_liters(input_val)
        elif func_name == 'liters_to_cubic_meters':
            result = liters_to_cubic_meters(input_val)
        elif func_name == 'kiloliters_to_liters':
            result = kiloliters_to_liters(input_val)
        elif func_name == 'gallons_us_to_cubic_meters':
            result = gallons_us_to_cubic_meters(input_val)
        print(f"{func_name}: {input_val} -> {result}")