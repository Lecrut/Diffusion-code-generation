def compare_lengths(a, b):
    if a > b:
        return (a, "greater")
    elif a < b:
        return (b, "greater")
    else:
        return (a, "equal")

if __name__ == '__main__':
    print(compare_lengths(5.0, 3.0))
    print(compare_lengths(2.5, 4.5))
    print(compare_lengths(3.3, 3.3))