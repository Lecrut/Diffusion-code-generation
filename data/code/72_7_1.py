def compare_lists(list1, list2):
    for a, b in zip(list1, list2):
        print(f"Comparing: {a} and {b}")
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]
    compare_lists(list_a, list_b)