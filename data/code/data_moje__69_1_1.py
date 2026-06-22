def miles_to_feet(miles):
    return [m * 5280 for m in miles]

if __name__ == '__main__':
    values = [1, 2, 5, 10, 0.5]
    result = miles_to_feet(values)
    print(result)