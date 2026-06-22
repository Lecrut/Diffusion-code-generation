def convert_miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError("Invalid input type. Please provide an integer or float.")
    return miles * 1.60934

if __name__ == '__main__':
    print(convert_miles_to_kilometers(5))