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
    item_to_remove_2 = "grape"
    print("Original list:", items)
    manager.remove_specific_item(items, item_to_remove_1)
    print("After removing", item_to_remove_1, ":", items)
    manager.remove_specific_item(items, item_to_remove_2)
    print("After attempting to remove", item_to_remove_2, ":", items)