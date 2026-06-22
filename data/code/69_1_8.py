def miles_to_feet(miles_list):
    return [mile * 5280 for mile in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.5, 100]
    feet_results = miles_to_feet(sample_miles)
    print(feet_results)