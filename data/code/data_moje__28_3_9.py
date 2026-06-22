def sort_two_floats(a, b):
    if min(a, b) == a:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    val1 = 3.14
    val2 = 1.59
    result = sort_two_floats(val1, val2)
    print(result)