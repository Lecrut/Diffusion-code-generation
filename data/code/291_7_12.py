def compare_miles_to_kilometers(miles, kilometers):
    conversion_factor = 1.60934
    if miles is None or kilometers is None:
        return None
    return miles * conversion_factor == kilometers

if __name__ == '__main__':
    result = compare_miles_to_kilometers(5, 8.0467)
    print(result)