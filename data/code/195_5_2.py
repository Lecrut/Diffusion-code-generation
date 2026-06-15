def find_first_mismatch(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] != list2[i]:
            yield i, list1[i], list2[i]
            return
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 99, 4, 5]
    result_generator = find_first_mismatch(list_a, list_b)
    print("Mismatch found:")
    for index, val_a, val_b in result_generator:
        print(f"Index: {index}, List A value: {val_a}, List B value: {val_b}")
    list_c = [1, 2, 3]
    list_d = [1, 2, 3, 4, 5]
    result_generator_2 = find_first_mismatch(list_c, list_d)
    print("\nSecond mismatch check:")
    try:
        for index, val_c, val_d in result_generator_2:
            print(f"Index: {index}, List C value: {val_c}, List D value: {val_d}")
    except StopIteration:
        print("No mismatch found within the overlapping length.")