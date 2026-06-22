def nautical_miles_to_kilometers(nautical_miles):
    if not isinstance(nautical_miles, (int, float)):
        raise TypeError("Input value must be numeric.")
    return round(nautical_miles * 1.852, 2)

if __name__ == '__main__':
    sample_value = 5
    print(f"{sample_value} nautical miles is {nautical_miles_to_kilometers(sample_value)} kilometers")