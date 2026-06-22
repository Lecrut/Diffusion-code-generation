def convert_miles_to_km(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError('Length must be a number')
    return miles * 1.60934

if __name__ == '__main__':
    print(convert_miles_to_km(1))
    print(convert_miles_to_km(5))