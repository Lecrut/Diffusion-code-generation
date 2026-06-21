class TupleMinFinder:
    @staticmethod
    def find_smallest(data):
        if not data:
            return None
        smallest = data[0]
        for element in data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_list = [(3, 2), (1, 5), (4, 1), (1, 9), (5, 3), (9, 2)]
    result = TupleMinFinder.find_smallest(sample_list)
    print(result)