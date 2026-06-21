class TupleAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_smallest_first_index(self):
        if not self.data:
            return None
        smallest = self.data[0]
        for element in self.data[1:]:
            if element[0] < smallest[0]:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_data = [(3, 'a'), (1, 'b'), (4, 'c'), (1, 'd'), (5, 'e'), (9, 'f'), (2, 'g')]
    analyzer = TupleAnalyzer(sample_data)
    smallest_tuple = analyzer.find_smallest_first_index()
    print(smallest_tuple)