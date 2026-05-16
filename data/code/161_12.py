class ItemList:
    def __init__(self, items):
        self.items = items
    def display_items(self):
        for item in self.items:
            print(item)
if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry", "Date"]
    my_list = ItemList(sample_data)
    my_list.display_items()