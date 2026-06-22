from typing import Union
LITERS_TO_MILLILITERS = 1000
MILLILITERS_TO_LITERS = 1 / LITERS_TO_MILLILITERS
CUBIC_METERS_TO_LITERS = 1000
LITERS_TO_CUBIC_METERS = 1 / CUBIC_METERS_TO_LITERS
LITERS_TO_GALLONS = 0.264172
GALLONS_TO_LITERS = 1 / LITERS_TO_GALLONS

def validate_volume(value: Union[float, int]) -> None:
    if value < 0:
        raise ValueError('Volume cannot be negative')

def liters_to_milliliters(liters: float) -> float:
    validate_volume(liters)
    return liters * LITERS_TO_MILLILITERS

def milliliters_to_liters(milliliters: float) -> float:
    validate_volume(milliliters)
    return milliliters * MILLILITERS_TO_LITERS

def cubic_meters_to_liters(cubic_meters: float) -> float:
    validate_volume(cubic_meters)
    return cubic_meters * CUBIC_METERS_TO_LITERS

def liters_to_cubic_meters(liters: float) -> float:
    validate_volume(liters)
    return liters * LITERS_TO_CUBIC_METERS

def liters_to_gallons(liters: float) -> float:
    validate_volume(liters)
    return liters * LITERS_TO_GALLONS

def gallons_to_liters(gallons: float) -> float:
    validate_volume(gallons)
    return gallons * GALLONS_TO_LITERS
if __name__ == '__main__':
    sample_liters = 5.0
    sample_milliliters = 1500.0
    sample_cubic_meters = 0.003
    sample_gallons = 1.0
    print(f'{sample_liters} L is {liters_to_milliliters(sample_liters)} mL')
    print(f'{sample_milliliters} mL is {milliliters_to_liters(sample_milliliters)} L')
    print(f'{sample_cubic_meters} m³ is {cubic_meters_to_liters(sample_cubic_meters)} L')
    print(f'{sample_liters} L is {liters_to_cubic_meters(sample_liters)} m³')
    print(f'{sample_liters} L is {liters_to_gallons(sample_liters)} gal')
    print(f'{sample_gallons} gal is {gallons_to_liters(sample_gallons)} L')