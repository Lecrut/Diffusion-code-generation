def calculate_intersection_and_union(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return intersection, union, size_difference

if __name__ == '__main__':
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7, 8}
    result = calculate_intersection_and_union(set_x, set_y)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Size Difference (Union - Intersection):", result[2])