def extend_list_in_place(list1, list2):
    list1.extend(list2)

if __name__ == '__main__':
    original_list = [1, 2, 3]
    additional_elements = [4, 5, 6]
    extend_list_in_place(original_list, additional_elements)
    print("Extended List:", original_list)