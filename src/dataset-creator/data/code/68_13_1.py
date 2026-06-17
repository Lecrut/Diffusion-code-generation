from typing import Union
CUBIC_METER_TO_LITER = 1000.0
LITER_TO_KILOLITER = 0.001
KILOLITER_TO_CUBIC_METERS = 0.001
GALLON_US_TO_LITER = 3.785411784
LITER_TO_GALLON_US = 1 / GALLON_US_TO_LITER
def cubic_meters_to_liters(value: float) -> float:
    return value * CUBIC_METER_TO_LITER
def liter_to_kiloliter(value: float) -> float:
    return value * LITER_TO_KILOLITER
def kiloliter_to_cubic_meters(value: float) -> float:
    return value * KILOLITER_TO_CUBIC_METERS
def gallons_us_to_liters(value: Union[float, int]) -> float:
    return value * GALLON_US_TO_LITER
def liters_to_gallons_us(value: Union[float, int]) -> float:
    return value * LITER_TO_GALLON_US
if __name__ == '__main__':
    sample_cubic_meters = 5.0
    result_liters = cubic_meters_to_liters(sample_cubic_meters)
    print(f"{sample_cubic_meters} m³ is {result_liters:.2f} L")
    kiliters = liter_to_kiloliter(result_liters / CUBIC_METER_TO_LITER * 10.0)
    cubic_from_kilo = kiloliter_to_cubic_meters(kiliters)
    print(f"{kiliters:.2f} kL is {cubic_from_kilo:.4f} m³")
    sample_gallons = 50
    result_liters_gal = gallons_us_to_liters(sample_gallons)
    print(f"{sample_gallons} US gal is {result_liters_gal:.2f} L")
    final_gallons = liters_to_gallons_us(result_liters / CUBIC_METER_TO_LITER * 10.0)
    print(f"{final_gallons:.4f} L is {sample_gallons + result_liters_gal - sample_gallons:.2f} US gal")