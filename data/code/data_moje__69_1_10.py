def miles_to_feet(miles_list):
    return [m * 5280 for m in miles_list]

if __name__ == '__main__':
    sample_miles = [1.0, 2.5, 10.0, 0.5, 100.0]
    result = miles_to_feet(sample_miles)
    print(result)