def convert_miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)) or miles < 0:
        raise ValueError("Input must be a non-negative number")
    return miles * 1.60934

if __name__ == '__main__':
    print(convert_miles_to_kilometers(5))
    print(convert_miles_to_kilometers(0))
    print(convert_miles_to_kilometers(10.2))