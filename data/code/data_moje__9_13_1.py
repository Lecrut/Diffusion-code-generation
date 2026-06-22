def liters_to_milliliters(liters: float) -> float:
    return liters * 1000.0

def milliliters_to_liters(milliliters: float) -> float:
    return milliliters / 1000.0

def cubic_meters_to_liters(cubic_meters: float) -> float:
    return cubic_meters * 1000.0

def liters_to_cubic_meters(liters: float) -> float:
    return liters / 1000.0

def liters_to_gallons(liters: float) -> float:
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    return gallons / 0.264172

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

def milliliters_to_cubic_meters(milliliters: float) -> float:
    liters = milliliters_to_liters(milliliters)
    return liters_to_cubic_meters(liters)

def cubic_meters_to_milliliters(cubic_meters: float) -> float:
    liters = cubic_meters_to_liters(cubic_meters)
    return liters_to_milliliters(liters)

if __name__ == '__main__':
    sample_liters = 2.5
    print(liters_to_milliliters(sample_liters))
    print(liters_to_gallons(sample_liters))
    print(liters_to_cubic_meters(sample_liters))
    
    sample_milliliters = 500.0
    print(milliliters_to_liters(sample_milliliters))
    print(milliliters_to_gallons(sample_milliliters))
    print(milliliters_to_cubic_meters(sample_milliliters))
    
    sample_cubic_meters = 0.5
    print(cubic_meters_to_liters(sample_cubic_meters))
    print(cubic_meters_to_gallons(sample_cubic_meters))
    print(cubic_meters_to_milliliters(sample_cubic_meters))
    
    sample_gallons = 10.0
    print(gallons_to_liters(sample_gallons))
    print(gallons_to_milliliters(sample_gallons))
    print(gallons_to_cubic_meters(sample_gallons))