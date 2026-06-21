class ArrayIndexer:
    def __init__(self, data):
        self.data = data

    def get_central(self):
        if not self.data:
            return None
        return self.data[len(self.data) // 2]

    @staticmethod
    def calculate_index(length):
        return length // 2

if __name__ == '__main__':
    numbers_odd = [15, 25, 35, 45, 55]
    numbers_even = [10, 20, 30, 40, 50, 60]
    empty_list = []

    indexer_odd = ArrayIndexer(numbers_odd)
    indexer_even = ArrayIndexer(numbers_even)
    indexer_empty = ArrayIndexer(empty_list)

    print(indexer_odd.get_central())
    print(indexer_even.get_central())
    print(indexer_empty.get_central())