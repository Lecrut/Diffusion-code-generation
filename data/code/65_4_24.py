class IndexSelector:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_element_at_index(self, index):
        for i, item in enumerate(self.iterable):
            if i == index:
                yield item

if __name__ == '__main__':
    sample_sequence = range(1000000)
    target_index_1 = 500000
    target_index_2 = 750000
    selector = IndexSelector(sample_sequence)

    for value in selector.get_element_at_index(target_index_1):
        print(f"Element at index {target_index_1}: {value}")

    for value in selector.get_element_at_index(target_index_2):
        print(f"Element at index {target_index_2}: {value}")