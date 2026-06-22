def sort_floats(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    sorted_values = sort_floats(val1, val2)
    print(sorted_values)