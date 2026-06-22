def miles_to_feet(miles):
    return [mile * 5280 for mile in miles]

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.5]
    result = miles_to_feet(sample_miles)
    print(result)