def miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)):
        raise ValueError("Invalid input type. Please provide a number.")
    return miles * 1.60934

if __name__ == '__main__':
    try:
        print(miles_to_kilometers(5))
        print(miles_to_kilometers('a'))
    except ValueError as e:
        print(e)