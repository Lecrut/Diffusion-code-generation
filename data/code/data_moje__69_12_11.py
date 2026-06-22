def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    sample_miles = 1.0
    result = miles_to_feet_calc(sample_miles)
    print(result)