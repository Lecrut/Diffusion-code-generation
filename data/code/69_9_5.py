import timeit
import random
class O1List:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, index):
        return self._data[index]
    def __len__(self):
        return len(self._data)
def benchmark(list_data, num_accesses):
    standard_list = list_data
    o1_list = O1List(list_data)
    time_standard = timeit.timeit(lambda: standard_list[random.randint(0, len(list_data) - 1)], number=num_accesses)
    time_o1 = timeit.timeit(lambda: o1_list[random.randint(0, len(list_data) - 1)], number=num_accesses)
    return time_standard, time_o1
if __name__ == '__main__':
    SAMPLE_SIZE = 1000000
    NUM_RUNS = 100000
    sample_data = [random.randint(0, 1000000) for _ in range(SAMPLE_SIZE)]
    time_std, time_o1 = benchmark(sample_data, NUM_RUNS)
    print(f"Sample Size: {SAMPLE_SIZE}")
    print(f"Number of Accesses per Test: {NUM_RUNS}")
    print(f"Time taken for standard Python list access: {time_std:.6f} seconds")
    print(f"Time taken for O(1) custom list access: {time_o1:.6f} seconds")