def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
if __name__ == '__main__':
    result1 = calculate_sum(1, 2, 3)
    print(f"Sum of (1, 2, 3): {result1}")
    result2 = calculate_sum(10, 20, 30, 40)
    print(f"Sum of (10, 20, 30, 40): {result2}")
    result3 = calculate_sum(5)
    print(f"Sum of (5): {result3}")
    result4 = calculate_sum()
    print(f"Sum of (): {result4}")