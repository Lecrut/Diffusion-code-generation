class ListFilter:
    @staticmethod
    def remove_item_from_list(input_list, item_to_remove):
        return [item for item in input_list if item != item_to_remove]

if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 2, 5]
    item_to_remove = 2
    new_list = ListFilter.remove_item_from_list(original_list, item_to_remove)
    print(f"Original list: {original_list}")
    print(f"Item to remove: {item_to_remove}")
    print(f"New list: {new_list}")