def find_largest(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the largest")
    elif b >= a and b >= c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
if __name__ == '__main__':
    find_largest(10, 5, 20)
    find_largest(3, 8, 1)
    find_largest(42, 15, 30)