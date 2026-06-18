def reorder_items(items):
    divisible_by_three = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible_by_three + others
if __name__ == '__main__':
    sample_data = [1, 9, 2, 6, 7, 8, 3, 4, 5, 10]
    result = reorder_items(sample_data)
    print(result)