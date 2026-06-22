def sort_descending(a: float, b: float) -> tuple:
    if a >= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    val1 = 15.5
    val2 = 23.8
    result = sort_descending(val1, val2)
    print(result)