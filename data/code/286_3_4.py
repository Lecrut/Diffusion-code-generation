def miles_to_kilometers(miles):
    if isinstance(miles, (int, float)):
        return miles * 1.60934
    else:
        raise ValueError('Invalid input type. Please provide a number.')
if __name__ == '__main__':
    try:
        print(miles_to_kilometers(5))
        print(miles_to_kilometers('a'))
    except ValueError as e:
        print(e)