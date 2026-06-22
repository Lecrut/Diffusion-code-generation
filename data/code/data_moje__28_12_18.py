def sort_two_floats(first, second):
    lower = min(first, second)
    upper = max(first, second)
    return [lower, upper]

if __name__ == '__main__':
    val1 = 9.99
    val2 = 1.01
    output = sort_two_floats(val1, val2)
    print(output)