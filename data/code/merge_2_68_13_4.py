from typing import Union
CUBIC_METER_TO_LITER: float = 1000.0
LITER_TO_KILOLITER: float = 0.001
KILOLITER_TO_CUBIC_METERS: float = 0.001
GALLON_US_TO_LITER: float = 3.785411784
def cubic_meters_to_liters(value: Union[int, float]) -> float:
    return value * CUBIC_METER_TO_LITER
def liters_to_kiloliters(value: Union[int, float]) -> float:
    return value * LITER_TO_KILOLITER
def kiloliters_to_cubic_meters(value: Union[int, float]) -> float:
    return value * KILOLITER_TO_CUBIC_METERS
def gallons_us_to_liters(value: Union[int, float]) -> float:
    return value * GALLON_US_TO_LITER
if __name__ == '__main__':
    sample_cm3 = 5.0
    result_liters = cubic_meters_to_liters(sample_cm3)
    sample_liters = 125.0
    result_kliters = liters_to_kiloliters(sample_liters)
    sample_kliters = 2.0
    result_cm3 = kiloliters_to_cubic_meters(sample_kliters)
    sample_gallons = 48.0
    result_liters_from_gal = gallons_us_to_liters(sample_gallons)
    print(f"{sample_cm3} m³ = {result_liters:.2f} L")
    print(f"{sample_liters} L = {result_kliters:.6f} kL")
    print(f"{sample_kliters} kL = {result_cm3:.4f} m³")
    print(f"{sample_gallons} US gal = {result_liters_from_gal:.2f} L")