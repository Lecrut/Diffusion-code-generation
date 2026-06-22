class NestedListCounter:
    def __init__(self):
        self.count = 0

    @staticmethod
    def count_elements(nested_list):
        counter = NestedListCounter()
        counter._traverse(nested_list)
        return counter.count

    def _traverse(self, element):
        if isinstance(element, list):
            for item in element:
                self._traverse(item)
        else:
            self.count += 1

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    result = NestedListCounter.count_elements(sample_list)
    print(result)