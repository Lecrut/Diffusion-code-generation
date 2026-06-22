class NestedListFlattener:
    def __init__(self, data):
        self._data = data
    
    def flatten_and_print(self):
        for item in self._data:
            if isinstance(item, list):
                self.flatten_and_print(item)
            else:
                print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flattener = NestedListFlattener(sample_data)
    flattener.flatten_and_print()