def calculate_set_operations(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return intersection, union, size_difference

if __name__ == '__main__':
    sample_set_a = {10, 20, 30, 40, 50}
    sample_set_b = {40, 50, 60, 70, 80}
    intersection_result, union_result, size_diff = calculate_set_operations(sample_set_a, sample_set_b)
    print("Intersection:", intersection_result)
    print("Union:", union_result)
    print("Difference in size (|Union| - |Intersection|):", size_diff)