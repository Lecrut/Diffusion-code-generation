def set_operations_and_comparison(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    intersection_size = len(intersection)
    union_size = len(union)
    difference = union_size - intersection_size
    return intersection, union, difference
if __name__ == '__main__':
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7, 8}
    intersection, union, diff = set_operations_and_comparison(set_x, set_y)
    print(f"Set X: {set_x}")
    print(f"Set Y: {set_y}")
    print(f"Intersection: {intersection}")
    print(f"Union: {union}")
    print(f"Difference in size (Union - Intersection): {diff}")