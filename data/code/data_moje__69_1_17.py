def miles_to_feet(miles_list):
    return [m * 5280 for m in miles_list]

if __name__ == '__main__':
    hard_coded_miles = [1.0, 2.5, 3.0, 10.0, 0.5]
    feet_results = miles_to_feet(hard_coded_miles)
    print(feet_results)