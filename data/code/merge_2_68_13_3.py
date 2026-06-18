from typing import Union
CUBIC_METER_TO_LITER = 1000.0
LITER_TO_KILOLITER = 0.001
KILOLITER_TO_CUBIC_METERS = 0.001
GALLON_US_TO_LITER = 3.785411784
LITER_TO_GALLON_US = 1 / GALLON_US_TO_LITER
def cubic_meters_to_liters(value: float) -> float:
    return value * CUBIC_METER_TO_LITER
def liters_to_kiloliters(value: float) -> float:
    return value * LITER_TO_KILOLITER
def kiloliters_to_cubic_meters(value: float) -> float:
    return value * KILOLITER_TO_CUBIC_METERS
def gallons_us_to_liters(value: Union[float, int]) -> float:
    return value * GALLON_US_TO_LITER
def liters_to_gallons_us(value: Union[float, int]) -> float:
    return value * LITER_TO_GALLON_US
if __name__ == '__main__':
    sample_cubic_meters = 5.0
    result_liters = cubic_meters_to_liters(sample_cubic_meters)
    sample_liters = 1234.56789
    result_kiloliters = liters_to_kiloliters(sample_liters)
    sample_gallons_us = 10.0
    result_liters_from_gal = gallons_us_to_liters(sample_gallons_us)
    print(f"{sample_cubic_meters} cubic meters is {result_liters:.2f} liters.")
    print(f"{sample_liters} liters is {result_kiloliters:.6f} kiloliters.")
    print(f"{sample_gallons_us} US gallons is {result_liters_from_gal:.4f} liters.")