from typing import Union

def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000

if __name__ == '__main__':
    sample_liters = 5.0
    sample_milliliters = 2000.0
    sample_gallons = 1.0
    sample_cubic_meters = 0.003

    print(f"{sample_liters} liters to milliliters: {liters_to_milliliters(sample_liters)}")
    print(f"{sample_milliliters} milliliters to liters: {milliliters_to_liters(sample_milliliters)}")
    print(f"{sample_liters} liters to gallons: {liters_to_gallons(sample_liters)}")
    print(f"{sample_gallons} gallons to liters: {gallons_to_liters(sample_gallons)}")
    print(f"{sample_cubic_meters} cubic meters to liters: {cubic_meters_to_liters(sample_cubic_meters)}")
    print(f"{sample_liters} liters to cubic meters: {liters_to_cubic_meters(sample_liters)}")