def find_middle_value(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    values = sorted([a, b, c])
    return values[1]

if __name__ == '__main__':
    print(find_middle_value(3, 1, 2))
    print(find_middle_value(5, 9, 7))
    print(find_middle_value(-1, -3, -2))