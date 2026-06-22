def calculate_set_operations(set_x, set_y):
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    size_difference = len(union) - len(intersection)
    return intersection, union, size_difference

if __name__ == '__main__':
    SAMPLE_SET_X = {10, 20, 30, 40, 50}
    SAMPLE_SET_Y = {40, 50, 60, 70, 80}
    
    intersection, union, size_difference = calculate_set_operations(SAMPLE_SET_X, SAMPLE_SET_Y)
    
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference in size (|Union| - |Intersection|):", size_difference)