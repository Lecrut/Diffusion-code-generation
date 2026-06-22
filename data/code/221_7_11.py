def bitwise_sort(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    print(f"Sorting (1, 5, 3): {bitwise_sort(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {bitwise_sort(10, -2, 7)}")
    print(f"Sorting (0.9, 0.3, 0.7): {bitwise_sort(0.9, 0.3, 0.7)}")