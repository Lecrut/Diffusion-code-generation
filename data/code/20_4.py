def check_elementwise_equality(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            yield False
        else:
            yield True
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [1, 2, 4]
    print("list_a vs list_b:")
    for result in check_elementwise_equality(list_a, list_b):
        print(result)
    print("\nlist_a vs list_c:")
    for result in check_elementwise_equality(list_a, list_c):
        print(result)