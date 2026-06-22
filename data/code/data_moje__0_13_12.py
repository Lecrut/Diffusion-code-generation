KILOMETERS_TO_MILES_FACTOR = 0.621371

def convert_km_to_miles(kilometers: float) -> float:
    return kilometers * KILOMETERS_TO_MILES_FACTOR

if __name__ == '__main__':
    result = convert_km_to_miles(5)
    print(result)