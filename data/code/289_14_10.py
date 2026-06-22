conversion_factor = 1.852

def nautical_miles_to_kilometers(nautical_miles):
    kilometers = nautical_miles * conversion_factor
    return round(kilometers, 2)

if __name__ == '__main__':
    sample_values = [10, 5.5, 3.75]
    for value in sample_values:
        result = nautical_miles_to_kilometers(value)
        print(f"{value} nautical miles is {result} kilometers")