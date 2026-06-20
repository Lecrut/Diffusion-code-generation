def compare_large_integers(a, b):
    size_a = len(str(a))
    size_b = len(str(b))
    if size_a > size_b:
        return (1, 0)
    elif size_b > size_a:
        return (0, 1)
    else:
        return (a < b, a > b)

if __name__ == '__main__':
    result1 = compare_large_integers(123456789, 987654321)
    print(result1)
    result2 = compare_large_integers(123, 1234)
    print(result2)