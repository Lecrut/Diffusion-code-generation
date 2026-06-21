class ListModifier:
    def __init__(self, original_list):
        self.original_list = original_list

    def remove_items(self, items_to_remove):
        items_set = set(items_to_remove)
        return [item for item in self.original_list if item not in items_set]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    modifier = ListModifier(sample_list)
    items_to_remove = [2, 4, 6, 8]
    result = modifier.remove_items(items_to_remove)
    print(result)