import sys
def compare_lists(list1, list2):
    try:
        if list1 == list2:
            return True
        else:
            return False
    except TypeError:
        return False
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [4, 3, 2, 1]
    list_d = [1, 2, 3, 5]
    list_e = "hello"
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")
    print(f"Comparing {list_a} and {list_d}: {compare_lists(list_a, list_d)}")
    print(f"Comparing {list_a} and {list_a}: {compare_lists(list_a, list_a)}")
    print(f"Comparing {list_a} and {list_e}: {compare_lists(list_a, list_e)}")