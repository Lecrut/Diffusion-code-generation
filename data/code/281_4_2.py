def find_sum_of_specific_values(*args):
    total = 0
    for value in args:
        total += value
    return total
if __name__ == '__main__':
    result1 = find_sum_of_specific_values(1, 2, 3)
    print(f"Sum of (1, 2, 3): {result1}")
    result2 = find_sum_of_specific_values(10, 20, 5)
    print(f"Sum of (10, 20, 5): {result2}")
    result3 = find_sum_of_specific_values()
    print(f"Sum of (): {result3}")
    result4 = find_sum_of_specific_values(5.5, 10.5)
    print(f"Sum of (5.5, 10.5): {result4}")