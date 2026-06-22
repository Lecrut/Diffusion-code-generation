def miles_to_feet(miles_list):
    return [int(miles) * 5280 for miles in miles_list]

if __name__ == '__main__':
    sample_miles = [1, 2, 5, 10, 20]
    result = miles_to_feet(sample_miles)
    print(result)