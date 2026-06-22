def miles_to_feet(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    result = miles_to_feet(10.5)
    print(result)