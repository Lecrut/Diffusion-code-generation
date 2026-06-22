MILES_TO_FEET_FACTOR = 5280

def miles_to_feet(miles: float) -> float:
    return miles * MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    print(miles_to_feet(1.0))
    print(miles_to_feet(0.25))
    print(miles_to_feet(5.5))