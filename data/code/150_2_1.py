class ItemManager:
    def remove_specific_item(self, item_list, item_to_remove):
        try:
            item_list.remove(item_to_remove)
        except ValueError:
            pass
if __name__ == '__main__':
    manager = ItemManager()
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove_1 = 3
    manager.remove_specific_item(sample_list, item_to_remove_1)
    print(sample_list)
    sample_list_2 = ['apple', 'banana', 'cherry', 'date']
    item_to_remove_2 = 'cherry'
    manager.remove_specific_item(sample_list_2, item_to_remove_2)
    print(sample_list_2)
    sample_list_3 = [10, 20, 30]
    item_to_remove_3 = 99
    manager.remove_specific_item(sample_list_3, item_to_remove_3)
    print(sample_list_3)