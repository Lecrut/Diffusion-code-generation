def sort_two_floats(a, b):
    lower_bound = min(a, b)
    upper_bound = max(a, b)
    return (lower_bound, upper_bound)

if __name__ == '__main__':
    val1 = -5.5
    val2 = 10.2
    output = sort_two_floats(val1, val2)
    print(output)