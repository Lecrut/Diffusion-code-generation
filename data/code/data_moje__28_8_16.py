def sort_pair(a, b):
    first = a
    second = b
    if a > b:
        first = b
        second = a
    return first, second

if __name__ == '__main__':
    value_a = 42
    value_b = 17
    sorted_values = sort_pair(value_a, value_b)
    print(sorted_values)