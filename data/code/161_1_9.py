class ItemProcessor:

    @staticmethod
    def create_unique_item_list(item_objects):
        item_names = {item.name for item in item_objects}
        return list(item_names)
if __name__ == '__main__':

    class Item:

        def __init__(self, name):
            self.name = name
    sample_items = [Item('banana'), Item('apple'), Item('cherry'), Item('date'), Item('elderberry'), Item('apple')]
    unique_item_list = ItemProcessor.create_unique_item_list(sample_items)
    print(unique_item_list)