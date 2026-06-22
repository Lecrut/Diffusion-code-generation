def convert_miles_to_feet(miles_list):
    feet_conversion_factor = 5280
    return [miles * feet_conversion_factor for miles in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2, 3, 5, 10]
    result = convert_miles_to_feet(sample_miles)
    print(result)