def compare_integers(a, b, c):
    print(f"Comparison between {a} and {b}:")
    if a > b:
        print("a is greater than b")
    elif a < b:
        print("a is less than b")
    else:
        print("a is equal to b")
    print(f"\nComparison between {b} and {c}:")
    if b > c:
        print("b is greater than c")
    elif b < c:
        print("b is less than c")
    else:
        print("b is equal to c")
    print(f"\nComparison between {a} and {c}:")
    if a > c:
        print("a is greater than c")
    elif a < c:
        print("a is less than c")
    else:
        print("a is equal to c")
if __name__ == '__main__':
    x = 10
    y = 25
    z = 10
    compare_integers(x, y, z)