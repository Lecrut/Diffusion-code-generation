class ListModifier:
    @staticmethod
    def remove_item(data_list, item_to_remove):
        return [x for x in data_list if x != item_to_remove]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item = 3
    new_list = ListModifier.remove_item(my_list, item)
    print(new_list)
    
    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    item_2 = 'c'
    new_list_2 = ListModifier.remove_item(my_list_2, item_2)
    print(new_list_2)
    
    my_list_3 = [10, 20, 30]
    item_3 = 5
    new_list_3 = ListModifier.remove_item(my_list_3, item_3)
    print(new_list_3)