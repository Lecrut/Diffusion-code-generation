from typing import Union
CUBIC_METER_TO_LITER: float = 1000.0
LITER_TO_KILOLITER: float = 0.001
KILOLITER_TO_GALLON_US: float = 264.172052358
GALLON_US_TO_KILOLITER: float = 1 / KILOLITER_TO_GALLON_US
def cubic_meters_to_liters(value: Union[int, float]) -> int:
    return round(value * CUBIC_METER_TO_LITER)
def liters_to_kiloliters(value: Union[int, float]) -> float:
    return value / 1000.0
def kiloliters_to_gallons_us(value: Union[int, float]) -> int:
    return round(value * KILOLITER_TO_GALLON_US)
if __name__ == '__main__':
    test_volume_m3 = 2.5
    result_liters = cubic_meters_to_liters(test_volume_m3)
    converted_kl = liters_to_kiloliters(result_liters)
    final_gallons = kiloliters_to_gallons_us(converted_kl)
    print(f"{test_volume_m3} m³ is {result_liters} L")
    print(f"{result_liters} L is {converted_kl:.6f} kL")
    print(f"{converted_kl:.6f} kL is {final_gallons} US gallons")