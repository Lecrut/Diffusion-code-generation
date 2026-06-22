def compare_lengths(a, b):
    if a > b:
        return (">", a, b)
    elif b > a:
        return ("<", b, a)
    else:
        return ("=", a, b)

if __name__ == '__main__':
    print(compare_lengths(3.14, 2.72))
    print(compare_lengths(1.0, 1.0))
    print(compare_lengths(0.5, 99.9))