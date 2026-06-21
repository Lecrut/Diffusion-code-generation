class UniqueItemFilter:
    def __init__(self, items):
        self.items = set(items)
    
    def remove_duplicates(self, item_to_remove):
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2]
    filter_instance = UniqueItemFilter(sample_list)
    filter_instance.remove_duplicates(3)
    print(filter_instance.items)