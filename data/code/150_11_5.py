class ListFilter:
    def __init__(self, input_list):
        self.input_list = input_list

    def remove_item(self, item_to_remove):
        new_list = [item for item in self.input_list if item != item_to_remove]
        return new_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5]
    filter_instance = ListFilter(sample_list)
    item_to_remove = 2
    filtered_list = filter_instance.remove_item(item_to_remove)
    print(f"Original list: {sample_list}")
    print(f"Item to remove: {item_to_remove}")
    print(f"New list: {filtered_list}")