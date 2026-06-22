def convert_miles_to_feet(miles_list):
    conversion_factor = 5280
    return [miles * conversion_factor for miles in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2, 3.5, 5]
    result = convert_miles_to_feet(sample_miles)
    print(result)