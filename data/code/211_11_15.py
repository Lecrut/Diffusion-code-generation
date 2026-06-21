SET_A = {1, 2, 3, 4}
SET_B = {4, 5, 6, 7}

def calculate_set_operations(set_a=SET_A, set_b=SET_B):
    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_to_b = set_a - set_b
    difference_b_to_a = set_b - set_a
    return intersection, union, difference_a_to_b, difference_b_to_a

if __name__ == '__main__':
    result = calculate_set_operations()
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (A to B):", result[2])
    print("Difference (B to A):", result[3])