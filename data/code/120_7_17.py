def is_identical(obj1, obj2):
    return obj1 == obj2

if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = [1, 2, 3]
    LIST_C = [1, 2, 4]

    result_a_b = is_identical(LIST_A, LIST_B)
    result_a_c = is_identical(LIST_A, LIST_C)

    print(f"List A is identical to List B: {result_a_b}")
    print(f"List A is identical to List C: {result_a_c}")