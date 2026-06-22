def calculate_area(side):
    if isinstance(side, (int, float)):
        return side * side
    else:
        raise ValueError('Input must be an integer or float')
if __name__ == '__main__':
    print(calculate_area(5))
    print(calculate_area(3.5))