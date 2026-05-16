def is_greater(a, b):
    return a > b
if __name__ == '__main__':
    result1 = is_greater(10, 5)
    print(f"is_greater(10, 5): {result1}")
    result2 = is_greater(5, 10)
    print(f"is_greater(5, 10): {result2}")
    result3 = is_greater(7.5, 7.5)
    print(f"is_greater(7.5, 7.5): {result3}")
    result4 = is_greater(-1, -5)
    print(f"is_greater(-1, -5): {result4}")