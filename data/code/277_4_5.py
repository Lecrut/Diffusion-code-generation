class NestedListCounter:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def count_items(self):
        total_count = 0
        for item in self.nested_list:
            if isinstance(item, list):
                total_count += self.count_items(item)
            else:
                total_count += 1
        return total_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    counter = NestedListCounter(sample_list)
    print(counter.count_items())