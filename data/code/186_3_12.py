class TupleSorter:
    def __init__(self, tuples):
        self.tuples = tuples
    
    def sort_by_second_desc(self):
        self.tuples.sort(key=lambda x: x[1], reverse=True)
        return self.tuples

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 1), (5, 0)]
    sorter = TupleSorter(sample_tuples)
    sorted_tuples = sorter.sort_by_second_desc()
    print(sorted_tuples)