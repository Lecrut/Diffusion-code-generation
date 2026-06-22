class ArrayProcessor:
    def __init__(self, collection):
        self._items = list(collection)
    def retrieve_initial_item(self):
        first = self._items[0]
        return first
if __name__ == '__main__':
    values = [7, 8, 9]
    processor = ArrayProcessor(values)
    result = processor.retrieve_initial_item()
    print(result)