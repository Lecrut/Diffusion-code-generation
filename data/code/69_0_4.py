def miles_to_feet(miles):
    conversion_factor = 5280
    return miles * conversion_factor

if __name__ == '__main__':
    sample_values = [0, 1, 0.5, 10.123, -1]
    for val in sample_values:
        result = miles_to_feet(val)
        print(result)