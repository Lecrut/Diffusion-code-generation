class IndexFinder:
    def __init__(self, indices):
        self.indices = indices

    def find_final_index(self):
        if not self.indices:
            return -1
        return max(self.indices)

if __name__ == '__main__':
    finder1 = IndexFinder([1, 5, 3, 8, 2])
    print(finder1.find_final_index())

    finder2 = IndexFinder([10, 20, 5])
    print(finder2.find_final_index())

    finder3 = IndexFinder([42])
    print(finder3.find_final_index())

    finder4 = IndexFinder([])
    print(finder4.find_final_index())