def compare_lengths(a, b):
    if a > b:
        return ("greater", a, b)
    elif a < b:
        return ("less", a, b)
    else:
        return ("equal", a, b)

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)
    result2 = compare_lengths(1.0, 2.0)
    print(result2)
    result3 = compare_lengths(4.0, 4.0)
    print(result3)