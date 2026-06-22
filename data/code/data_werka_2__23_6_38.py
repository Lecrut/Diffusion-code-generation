def calculate_set_operations(set_x, set_y):
    intersection = set_x & set_y
    union = set_x | set_y
    size_difference = len(union) - len(intersection)
    return size_difference

if __name__ == '__main__':
    sample_set_x = {10, 20, 30, 40, 50}
    sample_set_y = {40, 50, 60, 70, 80}
    result = calculate_set_operations(sample_set_x, sample_set_y)
    print(result)