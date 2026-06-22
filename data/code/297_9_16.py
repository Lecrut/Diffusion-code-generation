def convert_miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)) or miles < 0:
        raise ValueError('Invalid input: Miles must be a non-negative number')
    return miles * 1.60934
if __name__ == '__main__':
    try:
        print(convert_miles_to_kilometers(5))
        print(convert_miles_to_kilometers(-2))
    except ValueError as e:
        print(e)