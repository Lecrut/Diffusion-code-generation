def sort_two_floats(a, b):
    first = min(a, b)
    second = max(a, b)
    return first, second

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    result = sort_two_floats(val1, val2)
    print(result)