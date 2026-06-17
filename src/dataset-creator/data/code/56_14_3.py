import timeit
def find_print_index(sequence: list[int], target_value: int) -> int | None:
    for idx, val in enumerate(sequence):
        if val == target_value:
            return idx
    return None
class PerformanceOptimizer:
    def __init__(self, data_size: int = 10_000):
        self.data_size = data_size
    def generate_sample_data(self) -> list[int]:
        return [i for i in range(self.data_size)] + [999] * (self.data_size // 2)
def main():
    SAMPLE_SIZE = 50_000
    TARGET_VALUE = 42
    optimizer = PerformanceOptimizer(data_size=SAMPLE_SIZE)
    data_list = optimizer.generate_sample_data()
    start_time = timeit.default_timer()
    result_index = find_print_index(data_list, TARGET_VALUE)
    end_time = timeit.default_timer()
    print(result_index if result_index is not None else -1)
if __name__ == '__main__':
    main()