class ArrayFetcher:
    def __init__(self, array):
        self.array = array

    def get_last_element(self):
        if not self.array:
            return None
        return self.array[-1]

if __name__ == '__main__':
    sample_array_1 = [10, 20, 30, 40, 50]
    fetcher_1 = ArrayFetcher(sample_array_1)
    print("Last element of sample_array_1:", fetcher_1.get_last_element())

    sample_array_2 = ['a', 'b', 'c']
    fetcher_2 = ArrayFetcher(sample_array_2)
    print("Last element of sample_array_2:", fetcher_2.get_last_element())

    empty_array = []
    fetcher_empty = ArrayFetcher(empty_array)
    print("Last element of empty_array:", fetcher_empty.get_last_element())