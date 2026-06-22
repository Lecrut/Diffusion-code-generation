def calculate_sets(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return size_difference

if __name__ == '__main__':
    sample_set_x = {1, 2, 3, 4}
    sample_set_y = {3, 4, 5, 6}
    result = calculate_sets(sample_set_x, sample_set_y)
    print(result)