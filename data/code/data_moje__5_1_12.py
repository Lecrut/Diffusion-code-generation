def compare_lengths(a, b):
    if a > b:
        return ("greater", a, b)
    elif a < b:
        return ("less", a, b)
    else:
        return ("equal", a, b)

if __name__ == '__main__':
    result1 = compare_lengths(5.5, 3.2)
    print(result1)
    result2 = compare_lengths(1.0, 1.0)
    print(result2)
    result3 = compare_lengths(2.3, 7.8)
    print(result3)