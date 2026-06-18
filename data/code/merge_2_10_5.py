def reorder_by_divisibility(items):
    divisible = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible + others
if __name__ == '__main__':
    sample_data = [1, 9, 2, 6, 7, 3, 4, 8]
    result = reorder_by_divisibility(sample_data)
    print(result)