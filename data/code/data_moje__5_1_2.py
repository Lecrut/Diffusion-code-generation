def compare_lengths(a, b):
    if a > b:
        return (a, b, "greater")
    elif a < b:
        return (a, b, "less")
    else:
        return (a, b, "equal")

if __name__ == '__main__':
    result = compare_lengths(3.5, 2.8)
    print(result)