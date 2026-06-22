def convert_miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError("Invalid input type: miles must be a number")
    return miles * 1.60934

if __name__ == '__main__':
    sample_value = 5
    print(convert_miles_to_kilometers(sample_value))