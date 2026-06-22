def is_valid_number(value):
    return isinstance(value, (int, float))

def find_the_middle_value_among_three_transform(a, b, c):
    if not all((is_valid_number(x) for x in [a, b, c])):
        raise ValueError('All inputs must be numbers')
    sorted_values = sorted([a, b, c])
    return sorted_values[1]
if __name__ == '__main__':
    try:
        result = find_the_middle_value_among_three_transform(5, 3, 9)
        print(result)
    except ValueError as e:
        print(e)