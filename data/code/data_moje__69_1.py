def convert_miles_to_feet(miles_list):
    conversion_factor = 5280
    return [miles * conversion_factor for miles in miles_list]

if __name__ == '__main__':
    hard_coded_miles = [1, 2, 5, 10, 26.2]
    results = convert_miles_to_feet(hard_coded_miles)
    print(results)