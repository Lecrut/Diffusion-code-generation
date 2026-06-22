def sort_three_numbers(a, b, c):
    numbers = sorted([a, b, c])
    return numbers

if __name__ == '__main__':
    result1 = sort_three_numbers(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sort_three_numbers(100, -5, 30)
    print(f"Sorted (100, -5, 30): {result2}")
    result3 = sort_three_numbers(-1, -10, -5)
    print(f"Sorted (-1, -10, -5): {result3}")