def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000.0

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000.0

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000.0

def liters_to_gallons(liters: float) -> float:
    return liters / 3.78541

def gallons_to_liters(gallons: float) -> float:
    return gallons * 3.78541

def milliliters_to_gallons(milliliters: float) -> float:
    return milliliters / 3785.41

def gallons_to_milliliters(gallons: float) -> float:
    return gallons * 3785.41

def cubic_meters_to_gallons(cubic_meters: float) -> float:
    liters = cubic_meters_to_liters(cubic_meters)
    return liters_to_gallons(liters)

def gallons_to_cubic_meters(gallons: float) -> float:
    liters = gallons_to_liters(gallons)
    return liters_to_cubic_meters(liters)

if __name__ == '__main__':
    sample_liters = 2.5
    sample_gallons = 1.0
    sample_cubic_meters = 0.5

    print(liters_to_milliliters(sample_liters))
    print(milliliters_to_liters(sample_liters * 1000))
    print(cubic_meters_to_liters(sample_cubic_meters))
    print(liters_to_cubic_meters(sample_liters))
    print(liters_to_gallons(sample_liters))
    print(gallons_to_liters(sample_gallons))
    print(milliliters_to_gallons(500.0))
    print(gallons_to_milliliters(sample_gallons))
    print(cubic_meters_to_gallons(sample_cubic_meters))
    print(gallons_to_cubic_meters(sample_gallons))