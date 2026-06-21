def unique_item_names(item_objects):
    return list({item.name for item in item_objects})

if __name__ == '__main__':
    class Item:
        def __init__(self, name):
            self.name = name

    items = [Item('apple'), Item('banana'), Item('apple'), Item('orange')]
    print(unique_item_names(items))