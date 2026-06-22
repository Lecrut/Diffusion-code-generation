def sort_three(a, b, c):
    return sorted([a, b, c])

if __name__ == '__main__':
    result1 = sort_three(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sort_three(-10, 0, 3)
    print(f"Sorted (-10, 0, 3): {result2}")
    result3 = sort_three(7, 7, 7)
    print(f"Sorted (7, 7, 7): {result3}")