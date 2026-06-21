class UniqueItemListCreator:
    @staticmethod
    def create_unique_item_list(item_objects):
        return list(set(item_objects))

if __name__ == '__main__':
    sample_items = ["banana", "apple", "cherry", "date", "elderberry", "apple"]
    unique_items = UniqueItemListCreator.create_unique_item_list(sample_items)
    print(unique_items)