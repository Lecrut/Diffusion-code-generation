def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        raise ValueError("Cannot check proportion when any denominator is zero")
    return (a * d) == (b * c)

if __name__ == '__main__':
    print(are_in_proportion(10, 5, 20, 10))