def extend_list_in_place(list1, list2):
    list1.extend(list2)

if __name__ == '__main__':
    initial_values = [10, 20, 30]
    additional_elements = [40, 50, 60]
    extend_list_in_place(initial_values, additional_elements)
    print(initial_values)