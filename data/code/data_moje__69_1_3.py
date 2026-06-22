def miles_to_feet(miles_list):
    return [miles * 5280 for miles in miles_list]

if __name__ == '__main__':
    original_miles = [1, 2, 3, 5, 10]
    result = miles_to_feet(original_miles)
    print(result)