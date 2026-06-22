def nautical_miles_to_kilometers(nautical_miles):
    conversion_factor = 1.852
    kilometers = nautical_miles * conversion_factor
    return round(kilometers, 2)

if __name__ == '__main__':
    sample_values = [10, 5.5, 3.75]
    for value in sample_values:
        print(nautical_miles_to_kilometers(value))