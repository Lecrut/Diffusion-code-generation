class ListModifier:
    @staticmethod
    def remove_duplicates(data_list, item_to_remove):
        return [item for item in data_list if item != item_to_remove]

if __name__ == '__main__':
    modifier = ListModifier()
    my_list = [1, 2, 3, 4, 5]
    item = 3
    new_list = modifier.remove_duplicates(my_list, item)
    print(new_list)

    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    item_2 = 'c'
    new_list_2 = modifier.remove_duplicates(my_list_2, item_2)
    print(new_list_2)

    my_list_3 = [10, 20, 30]
    item_3 = 5
    new_list_3 = modifier.remove_duplicates(my_list_3, item_3)
    print(new_list_3)