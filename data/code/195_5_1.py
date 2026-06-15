def find_first_mismatch(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] != list2[i]:
            yield i, list1[i], list2[i]
            return
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 9, 4, 5]
    result_generator = find_first_mismatch(list_a, list_b)
    for index, val_a, val_b in result_generator:
        print(f"Index: {index}, List A value: {val_a}, List B value: {val_b}")
    list_c = [10, 20, 30]
    list_d = [10, 20, 40]
    result_generator2 = find_first_mismatch(list_c, list_d)
    for index, val_c, val_d in result_generator2:
        print(f"Index: {index}, List C value: {val_c}, List D value: {val_d}")
    list_e = [1, 2]
    list_f = [1, 2, 3]
    result_generator3 = find_first_mismatch(list_e, list_f)
    try:
        for index, val_e, val_f in result_generator3:
            print(f"Index: {index}, List E value: {val_e}, List F value: {val_f}")
    except StopIteration:
        pass