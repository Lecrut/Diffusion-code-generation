def is_greater_than(a, b):
    return a > b

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 8),
        (7, 7)
    ]
    for value_pair in sample_values:
        result = is_greater_than(*value_pair)
        print(result)