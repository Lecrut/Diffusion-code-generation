def sort_two_floats(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    val1 = 5.3
    val2 = 2.1
    result = sort_two_floats(val1, val2)
    print(result)