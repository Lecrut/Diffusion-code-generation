def reorder_divisible_by_three(items):
    divisible = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible + others
if __name__ == '__main__':
    sample_data = [12, 5, 9, 7, 18, 4, 6]
    result = reorder_divisible_by_three(sample_data)
    print(result)