def miles_to_kilometers(miles):
    if isinstance(miles, (int, float)):
        return miles * 1.60934
    else:
        raise ValueError('Invalid input type. Please provide an integer or float.')
if __name__ == '__main__':
    print(miles_to_kilometers(5))
    print(miles_to_kilometers(10))