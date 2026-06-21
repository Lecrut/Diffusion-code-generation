class TupleListProcessor:
    def __init__(self, data):
        self.data = data

    def find_smallest_first_index(self):
        if not self.data:
            return None
        smallest = self.data[0]
        for element in self.data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_list = [(5, 2), (3, 4), (1, 6), (7, 8)]
    processor = TupleListProcessor(sample_list)
    result = processor.find_smallest_first_index()
    print(result)