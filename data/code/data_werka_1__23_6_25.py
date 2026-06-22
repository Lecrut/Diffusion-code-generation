def calculate_intersection_and_union(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return size_difference

if __name__ == '__main__':
    sample_set_x = {1, 2, 3, 4, 5}
    sample_set_y = {4, 5, 6, 7, 8}
    result = calculate_intersection_and_union(sample_set_x, sample_set_y)
    print(result)