def find_first_mismatch(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] != list2[i]:
            yield i, list1[i], list2[i]
            return
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 99, 4, 5]
    result_generator = find_first_mismatch(list_a, list_b)
    for index, val_a, val_b in result_generator:
        print(f"Index: {index}, List A element: {val_a}, List B element: {val_b}")