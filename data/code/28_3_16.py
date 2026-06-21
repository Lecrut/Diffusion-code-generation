def sort_two_floats(a: float, b: float) -> tuple:
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    result = sort_two_floats(val1, val2)
    print(result)