class ItemList:
    def __init__(self, items):
        self.items = items
    def display(self):
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item}")
if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    my_list = ItemList(sample_data)
    my_list.display()