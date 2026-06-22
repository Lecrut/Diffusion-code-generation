def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 0.0, -3.14]
    for value in sample_values:
        result = miles_to_feet_calc(value)
        print(result)