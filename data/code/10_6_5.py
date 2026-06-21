class ArrayProcessor:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def get_first_element(self):
        return self.items[0]

    def get_item_count(self):
        return len(self.items)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    handler = ArrayProcessor(sample_list)
    first_item = handler.get_first_element()
    total_items = handler.get_item_count()
    print(first_item)
    print(total_items)