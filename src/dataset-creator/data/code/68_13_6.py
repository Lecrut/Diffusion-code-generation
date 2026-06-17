from typing import Union
CUBIC_METER_TO_LITER = 1000.0
LITER_TO_CUBIC_METER = 0.001
KILOLITER_TO_CUBIC_METER = 1.0
GALLON_US_TO_LITER = 3.785411784
def cubic_meters_to_liters(value: float) -> Union[float, int]:
    return value * CUBIC_METER_TO_LITER
def liters_to_cubic_meters(value: float) -> Union[float, int]:
    return value / CUBIC_METER_TO_LITER
def kiloliters_to_cubic_meters(value: float) -> Union[float, int]:
    return value / KILOLITER_TO_CUBIC_METER
def gallons_us_to_liters(value: float) -> Union[float, int]:
    return value * GALLON_US_TO_LITER
if __name__ == '__main__':
    sample_cm3 = 5.0
    sample_liters = cubic_meters_to_liters(sample_cm3)
    sample_kl = liters_to_cubic_meters(125000.0) / KILOLITER_TO_CUBIC_METER
    sample_gallons = gallons_us_to_liters(473.0)
    print(f"{sample_cm3} cubic meters is {sample_liters} liters.")
    print(f"125,000 liters is {sample_kl} kiloliters.")
    print(f"473 US gallons is {sample_gallons} liters.")