def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    a = 10
    b = 25
    c = 10
    largest = find_largest(a, b, c)
    print(f"The largest number among {a}, {b}, and {c} is: {largest}")