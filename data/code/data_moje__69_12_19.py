def miles_to_feet_calc(miles: float) -> float:
    feet_per_mile: float = 5280.0
    return miles * feet_per_mile

if __name__ == '__main__':
    sample_miles: float = 3.5
    result: float = miles_to_feet_calc(sample_miles)
    print(result)