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
    time_standard = timeit.timeit(lambda: standard_list[random.randint(0, len(standard_list) - 1)], number=num_accesses)
    time_o1 = timeit.timeit(lambda: o1_list[random.randint(0, len(o1_list) - 1)], number=num_accesses)
    return time_standard, time_o1
if __name__ == '__main__':
    SAMPLE_SIZE = 1000000
    NUM_RUNS = 100000
    sample_data = list(range(SAMPLE_SIZE))
    time_std, time_o1 = benchmark(sample_data, NUM_RUNS)
    print(f"Sample Size: {SAMPLE_SIZE}")
    print(f"Number of Accesses per Test: {NUM_RUNS}")
    print("-" * 30)
    print(f"Time taken for standard Python list access: {time_std:.6f} seconds")
    print(f"Time taken for O(1) index access structure: {time_o1:.6f} seconds")
    if time_o1 < time_std:
        speedup = time_std / time_o1
        print(f"Speedup factor: {speedup:.2f}x")
    else:
        print("O(1) structure was slower (this is unexpected for simple indexing).")