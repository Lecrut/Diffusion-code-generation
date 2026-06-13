class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
def print_item_details(items):
    for item in items:
        print(f"Name: {item.name}, Value: {item.value}")
if __name__ == '__main__':
    sample_list = [Item("Apple", 10), Item("Banana", 20), Item("Cherry", 30)]
    print_item_details(sample_list)