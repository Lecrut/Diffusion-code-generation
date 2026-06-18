def reorder_divisible_by_three(items):
    divisible = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible + others
if __name__ == '__main__':
    sample_data = [1, 9, 2, 6, 7, 3, 4, 8]
    result = reorder_divisible_by_three(sample_data)
    print(result)