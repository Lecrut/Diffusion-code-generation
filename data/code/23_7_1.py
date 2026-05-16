def set_operations_comparison(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    intersection_size = len(intersection)
    union_size = len(union)
    difference = union_size - intersection_size
    return intersection, union, difference
if __name__ == '__main__':
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7, 8}
    intersection_result, union_result, diff_result = set_operations_comparison(set_x, set_y)
    print(f"Set X: {set_x}")
    print(f"Set Y: {set_y}")
    print(f"Intersection: {intersection_result}")
    print(f"Union: {union_result}")
    print(f"Difference in size (Union size - Intersection size): {diff_result}")