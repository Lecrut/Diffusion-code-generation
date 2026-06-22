def miles_to_feet(miles_list):
    return [int(miles) * 5280 for miles in miles_list]

if __name__ == '__main__':
    miles_data = [1, 2, 5, 10]
    feet_data = miles_to_feet(miles_data)
    print(feet_data)