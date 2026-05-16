class ItemManager:
    def remove_specific_item(self, item_list, item_to_remove):
        try:
            item_list.remove(item_to_remove)
        except ValueError:
            pass
if __name__ == '__main__':
    manager = ItemManager()
    items = ["apple", "banana", "cherry", "apple", "date"]
    item_to_remove_1 = "apple"
    print("Original list:", items)
    manager.remove_specific_item(items, item_to_remove_1)
    print("After removing first 'apple':", items)
    items2 = ["red", "green", "blue", "red"]
    item_to_remove_2 = "red"
    print("Original list:", items2)
    manager.remove_specific_item(items2, item_to_remove_2)
    print("After removing 'red' from second list:", items2)
    items3 = ["a", "b", "c"]
    item_to_remove_3 = "z"
    print("Original list:", items3)
    manager.remove_specific_item(items3, item_to_remove_3)
    print("After attempting to remove 'z':", items3)