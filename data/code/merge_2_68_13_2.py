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
    sample_cubic_meters = 2.5
    result_liters = cubic_meters_to_liters(sample_cubic_meters)
    print(f"{sample_cubic_meters} m³ is {result_liters:.4f} L")
    converted_kiloliters = liters_to_kiloliters(result_liters)
    print(f"{converted_kiloliters:.6f} kL")
    sample_gallons_us = 10.5
    result_from_gallons = gallons_us_to_liters(sample_gallons_us)
    print(f"{sample_gallons_us} gal is {result_from_gallons:.4f} L")