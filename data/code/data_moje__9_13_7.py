def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000.0

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000.0

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000.0

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

def milliliters_to_cubic_meters(milliliters: float) -> float:
    liters = milliliters_to_liters(milliliters)
    return liters_to_cubic_meters(liters)

def cubic_meters_to_milliliters(cubic_meters: float) -> float:
    liters = cubic_meters_to_liters(cubic_meters)
    return liters_to_milliliters(liters)

def milliliters_to_gallons(milliliters: float) -> float:
    liters = milliliters_to_liters(milliliters)
    return liters_to_gallons(liters)

def gallons_to_milliliters(gallons: float) -> float:
    liters = gallons_to_liters(gallons)
    return liters_to_milliliters(liters)

def cubic_meters_to_gallons(cubic_meters: float) -> float:
    liters = cubic_meters_to_liters(cubic_meters)
    return liters_to_gallons(liters)

def gallons_to_cubic_meters(gallons: float) -> float:
    liters = gallons_to_liters(gallons)
    return liters_to_cubic_meters(liters)

if __name__ == '__main__':
    sample_liters = 5.0
    sample_milliliters = 250.0
    sample_cubic_meters = 0.001
    sample_gallons = 1.5

    print(liters_to_milliliters(sample_liters))
    print(milliliters_to_liters(sample_milliliters))
    print(liters_to_cubic_meters(sample_liters))
    print(cubic_meters_to_liters(sample_cubic_meters))
    print(liters_to_gallons(sample_liters))
    print(gallons_to_liters(sample_gallons))
    print(milliliters_to_cubic_meters(sample_milliliters))
    print(cubic_meters_to_milliliters(sample_cubic_meters))
    print(milliliters_to_gallons(sample_milliliters))
    print(gallons_to_milliliters(sample_gallons))
    print(cubic_meters_to_gallons(sample_cubic_meters))
    print(gallons_to_cubic_meters(sample_gallons))