def compare_miles_to_kilometers(miles, kilometers):
    conversion_factor = 1.60934
    if miles == kilometers / conversion_factor:
        return 'Equal'
    elif miles > kilometers / conversion_factor:
        return 'More Miles'
    else:
        return 'More Kilometers'
if __name__ == '__main__':
    result = compare_miles_to_kilometers(5, 8.0467)
    print(result)