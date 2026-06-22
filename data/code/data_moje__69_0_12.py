def miles_to_feet(miles):
    return miles * 5280.0

if __name__ == '__main__':
    test_values = [1.0, 0.5, 10.25, 100.0]
    for value in test_values:
        result = miles_to_feet(value)
        print(f"{value} miles is {result} feet")