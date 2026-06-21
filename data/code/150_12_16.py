class ItemListManager:
    def __init__(self, initial_list):
        self.items = list(initial_list)

    @staticmethod
    def _is_index(target):
        return isinstance(target, int) and 0 <= target < len(self.items)

    def remove_item(self, item_to_remove):
        if self._is_index(item_to_remove):
            self.items.pop(item_to_remove)
        elif item_to_remove in self.items:
            self.items.remove(item_to_remove)

if __name__ == '__main__':
    initial_data = ["apple", "banana", "apple", "orange", "banana"]
    manager = ItemListManager(initial_data)
    print("Initial list:", manager.items)
    item_to_remove_1 = "apple"
    manager.remove_item(item_to_remove_1)
    print(f"After removing first '{item_to_remove_1}':", manager.items)
    item_to_remove_2 = 3
    manager.remove_item(item_to_remove_2)
    print(f"After removing index {item_to_remove_2}: {manager.items}")
    item_to_remove_3 = "grape"
    manager.remove_item(item_to_remove_3)
    print(f"After attempting to remove '{item_to_remove_3}':", manager.items)