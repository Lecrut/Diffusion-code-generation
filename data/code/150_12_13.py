class ItemListManager:
    def __init__(self, initial_list):
        self.items = list(initial_list)

    @staticmethod
    def _is_valid_index(lst, index):
        return isinstance(index, int) and 0 <= index < len(lst)

    @staticmethod
    def _remove_by_value(lst, value):
        if value in lst:
            return [item for item in lst if item != value]
        else:
            raise ValueError('Target not found in list')

    @staticmethod
    def _remove_by_index(lst, index):
        if ItemListManager._is_valid_index(lst, index):
            return lst[:index] + lst[index + 1:]
        else:
            raise IndexError('Index out of range')

    def remove_item(self, target):
        if isinstance(target, int):
            return self._remove_by_index(self.items, target)
        else:
            return self._remove_by_value(self.items, target)

if __name__ == '__main__':
    initial_data = ["apple", "banana", "apple", "orange", "banana"]
    manager = ItemListManager(initial_data)
    print("Initial list:", manager.items)
    item_to_remove_1 = "apple"
    manager.remove_item(item_to_remove_1)
    print(f"After removing first '{item_to_remove_1}':", manager.items)
    item_to_remove_2 = "banana"
    manager.remove_item(item_to_remove_2)
    print(f"After removing first '{item_to_remove_2}':", manager.items)
    item_to_remove_3 = 0
    manager.remove_item(item_to_remove_3)
    print(f"After removing by index {item_to_remove_3}:", manager.items)