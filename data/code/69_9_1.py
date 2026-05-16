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
    number_of_runs = 10000
    time_o1 = timeit.timeit(lambda: o1_list[N // 2], number=number_of_runs) / number_of_runs
    time_standard = timeit.timeit(lambda: standard_list[N // 2], number=number_of_runs) / number_of_runs
    print(f"List Size: {N}")
    print(f"O(1) Access Time (Average over {number_of_runs} runs): {time_o1:.9f} seconds")
    print(f"Standard List Access Time (Average over {number_of_runs} runs): {time_standard:.9f} seconds")