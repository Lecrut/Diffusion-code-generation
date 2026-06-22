def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280

if __name__ == '__main__':
    sample_miles: float = 2.5
    result: float = miles_to_feet_calc(sample_miles)
    print(result)