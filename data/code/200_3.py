class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
def print_object_details(data_list):
    for item in data_list:
        print(f"Name: {item.name}, Value: {item.value}")
if __name__ == '__main__':
    sample_data = [Item("Apple", 10), Item("Banana", 20), Item("Cherry", 30)]
    print_object_details(sample_data)