def miles_to_feet(miles_list):
    return [miles * 5280 for miles in miles_list]

if __name__ == '__main__':
    mile_values = [1, 2, 5, 10, 15]
    result = miles_to_feet(mile_values)
    print(result)