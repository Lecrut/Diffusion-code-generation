class NestedListCounter:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def count_elements(self):
        count = 0
        for element in self.nested_list:
            if isinstance(element, list):
                count += self.count_elements(element)
            else:
                count += 1
        return count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    counter = NestedListCounter(sample_list)
    result = counter.count_elements()
    print(result)