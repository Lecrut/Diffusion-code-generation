def find_largest(a, b, c):
    if a >= b and a >= c:
        print(f"Largest: {a}")
    elif b >= a and b >= c:
        print(f"Largest: {b}")
    else:
        print(f"Largest: {c}")
if __name__ == '__main__':
    find_largest(10, 5, 20)
    find_largest(3, 8, 1)
    find_largest(7, 7, 7)
    find_largest(42, 15, 30)