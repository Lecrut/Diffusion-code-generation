def calculate_intersection_and_union(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    difference_in_size = abs(len(intersection) - len(union))
    return intersection, union, difference_in_size

if __name__ == '__main__':
    set_x = {1, 2, 3, 4}
    set_y = {3, 4, 5, 6}
    intersection, union, difference_in_size = calculate_intersection_and_union(set_x, set_y)
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference in Size:", difference_in_size)