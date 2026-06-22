def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    print(miles_to_feet_calc(1.0))
    print(miles_to_feet_calc(0.5))
    print(miles_to_feet_calc(10.0))