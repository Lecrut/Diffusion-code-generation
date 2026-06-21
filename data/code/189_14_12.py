class ListModifier:
    @staticmethod
    def remove_by_reference(data_list, item):
        if item in data_list:
            data_list.remove(item)
        else:
            raise ValueError(f"Item '{item}' not found in the list.")

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    item_to_remove = 30
    try:
        ListModifier.remove_by_reference(my_list, item_to_remove)
        print("List after removing", item_to_remove, ":", my_list)
    except ValueError as e:
        print(e)