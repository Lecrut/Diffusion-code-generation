def sort_three(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    print(f"Sorting (1, 5, 3): {sort_three(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sort_three(10, -2, 7)}")
    print(f"Sorting (-3.5, 0, 1.2): {sort_three(-3.5, 0, 1.2)}")