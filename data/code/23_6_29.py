def calculate_set_operations(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return intersection, union, size_difference

if __name__ == '__main__':
    set_x = {1, 2, 3, 4}
    set_y = {3, 4, 5, 6}
    intersection, union, size_difference = calculate_set_operations(set_x, set_y)
    print("Intersection:", intersection)
    print("Union:", union)
    print("Size Difference (Union - Intersection):", size_difference)