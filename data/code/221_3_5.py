def sort_three_numbers(a, b, c):
    return sorted([a, b, c])

if __name__ == '__main__':
    result1 = sort_three_numbers(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sort_three_numbers(-10, 0, 3)
    print(f"Sorted (-10, 0, 3): {result2}")
    result3 = sort_three_numbers(7, 7, 7)
    print(f"Sorted (7, 7, 7): {result3}")