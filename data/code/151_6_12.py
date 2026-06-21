def extend_list_in_place(list1, list2):
    list1.extend(list2)

if __name__ == '__main__':
    initial_list = [20, 21, 22]
    additional_elements = [23, 24, 25]
    extend_list_in_place(initial_list, additional_elements)
    print(initial_list)