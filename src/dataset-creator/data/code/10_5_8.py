def reorder_items(items):
    divisible_by_three = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible_by_three + others
if __name__ == '__main__':
    sample_list = [1, 9, 2, 6, 5, 8, 7, 3, 4]
    result = reorder_items(sample_list)
    print(result)