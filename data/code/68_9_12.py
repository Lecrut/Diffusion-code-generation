def find_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be numbers')
    return abs(a - b)
if __name__ == '__main__':
    try:
        print(find_difference(10, 5))
        print(find_difference(-3, 7))
        print(find_difference(3.5, 2.1))
        print(find_difference('a', 5))
    except ValueError as e:
        print(e)