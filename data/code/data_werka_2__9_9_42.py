from typing import Union

def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

if __name__ == '__main__':
    sample_liters = 5.0
    sample_milliliters = 1500.0
    sample_cubic_meters = 0.003
    sample_gallons = 1.0

    print(f"{sample_liters} liters is {liters_to_milliliters(sample_liters)} milliliters")
    print(f"{sample_milliliters} milliliters is {milliliters_to_liters(sample_milliliters)} liters")
    print(f"{sample_cubic_meters} cubic meters is {cubic_meters_to_liters(sample_cubic_meters)} liters")
    print(f"{sample_liters} liters is {liters_to_gallons(sample_liters)} gallons")
    print(f"{sample_gallons} gallons is {gallons_to_liters(sample_gallons)} liters")