import timeit
class O1List:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, index):
        return self._data[index]
    def __len__(self):
        return len(self._data)
class StandardList:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, index):
        return self._data[index]
if __name__ == '__main__':
    N = 1000000
    sample_data = list(range(N))
    o1_list = O1List(sample_data)
    standard_list = StandardList(sample_data)
    num_runs = 10000
    time_o1 = timeit.timeit(lambda: o1_list[N // 2], number=num_runs)
    time_standard = timeit.timeit(lambda: standard_list[N // 2], number=num_runs)
    print(f"List Size (N): {N}")
    print(f"Number of Runs: {num_runs}")
    print(f"Time taken for O(1) access (O1List): {time_o1:.6f} seconds")
    print(f"Time taken for Standard List access: {time_standard:.6f} seconds")