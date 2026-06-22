def nautical_miles_to_kilometers(nautical_miles):
    if not isinstance(nautical_miles, (int, float)):
        raise TypeError("Input value must be numeric.")
    kilometers = nautical_miles * 1.852
    return round(kilometers, 2)

if __name__ == '__main__':
    sample_value = 5.0
    result = nautical_miles_to_kilometers(sample_value)
    print(result)