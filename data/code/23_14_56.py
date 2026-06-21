def compare_values(a, b):

    def validate_input(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError('Both arguments must be integers or floats.')
    validate_input(a, b)
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    result1 = compare_values(10, 5)
    print(result1)
    result2 = compare_values(7, 7)
    print(result2)
    result3 = compare_values(3.5, 4.2)
    print(result3)