def compare_list_sizes(list_a, list_b):
    size_a = len(list_a)
    size_b = len(list_b)
    if size_a > size_b:
        print("List A is larger.")
    elif size_b > size_a:
        print("List B is larger.")
    else:
        print("Both lists have the same size.")
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30]
    compare_list_sizes(list_a, list_b)
    list_c = [5, 5, 5]
    list_d = [5, 5, 5]
    compare_list_sizes(list_c, list_d)
    list_e = []
    list_f = [1]
    compare_list_sizes(list_e, list_f)