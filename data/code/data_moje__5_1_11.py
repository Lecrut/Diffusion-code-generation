def compare_lengths(a: float, b: float) -> tuple:
    if a > b:
        return (1, a, b)
    elif a < b:
        return (-1, a, b)
    else:
        return (0, a, b)

if __name__ == '__main__':
    print(compare_lengths(3.5, 2.1))
    print(compare_lengths(1.0, 1.0))
    print(compare_lengths(0.5, 5.0))