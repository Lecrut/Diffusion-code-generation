def miles_to_feet(miles):
    return [m * 5280 for m in miles]

if __name__ == '__main__':
    mile_values = [1, 2, 5, 10]
    feet_values = miles_to_feet(mile_values)
    print(feet_values)