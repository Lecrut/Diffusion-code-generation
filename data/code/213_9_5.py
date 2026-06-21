class ListFlattener:
    def __init__(self):
        self.result = []

    def flatten(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.flatten(item)
            else:
                self.result.append(item)

if __name__ == '__main__':
    flattener = ListFlattener()
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    flattener.flatten(sample_list)
    print(flattener.result)