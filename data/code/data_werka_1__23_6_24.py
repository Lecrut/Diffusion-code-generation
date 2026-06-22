def calculate_intersection_union(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    difference_in_size = abs(len(intersection) - len(union))
    return intersection, union, difference_in_size

if __name__ == '__main__':
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7, 8}
    intersection, union, difference_in_size = calculate_intersection_union(set_x, set_y)
    print(intersection)
    print(union)
    print(difference_in_size)