def convert_miles_to_feet(mile_values):
    feet_conversion_factor = 5280
    return [miles * feet_conversion_factor for miles in mile_values]

if __name__ == '__main__':
    sample_miles = [1, 5, 10, 15, 20]
    result = convert_miles_to_feet(sample_miles)
    print(result)