def convert_kilometers_to_meters(km: float) -> float:
    return km * 1000

def convert_kilometers_to_miles(km: float) -> float:
    return km * 0.621371

def convert_kilometers_to_feet(km: float) -> float:
    return km * 3280.84

if __name__ == '__main__':
    distance_km = 5
    print(f"{distance_km} kilometers is {convert_kilometers_to_meters(distance_km)} meters")
    print(f"{distance_km} kilometers is {convert_kilometers_to_miles(distance_km)} miles")
    print(f"{distance_km} kilometers is {convert_kilometers_to_feet(distance_km)} feet")