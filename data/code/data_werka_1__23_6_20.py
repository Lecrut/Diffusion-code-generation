def calculate_intersection_and_union(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    return intersection, union

if __name__ == '__main__':
    set_x = {1, 2, 3, 4, 5}
    set_y = {4, 5, 6, 7, 8}
    
    intersection, union = calculate_intersection_and_union(set_x, set_y)
    
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference in size (|Union| - |Intersection|):", len(union) - len(intersection))