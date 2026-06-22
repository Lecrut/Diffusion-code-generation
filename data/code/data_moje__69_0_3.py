def miles_to_feet(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    distance_in_feet = miles_to_feet(1.5)
    print(distance_in_feet)