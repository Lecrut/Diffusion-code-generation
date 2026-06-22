def calculate_feet(miles_list):
    feet_per_mile = 5280
    return [miles * feet_per_mile for miles in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 0.5, 10]
    results = calculate_feet(sample_miles)
    print(results)