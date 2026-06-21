def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            return False
    return True

if __name__ == '__main__':
    list_a = [1, 5, 3, 7, 9]
    list_b = [1, 5, 4, 7, 9]
    result = compare_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    if not result:
        print("Lists are different.")
    else:
        print("Lists are identical.")