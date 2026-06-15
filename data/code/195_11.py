def list_comparison(list1, list2):
    return list1 == list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [3, 2, 1]
    list_d = [1, 2, 4]
    print(f"list_a == list_b: {list_comparison(list_a, list_b)}")
    print(f"list_a == list_c: {list_comparison(list_a, list_c)}")
    print(f"list_a == list_d: {list_comparison(list_a, list_d)}")