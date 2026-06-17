import timeit
class PrintIndexProcessor:
    def __init__(self):
        self.data = [10, 25, 30, 45, 60]
    def find_target_index(self, target_value=45):
        for index in range(len(self.data)):
            if self.data[index] == target_value:
                return index
        return -1
def run_benchmark():
    processor = PrintIndexProcessor()
    start_time = timeit.default_timer()
    result_index = processor.find_target_index(45)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time
    print(f"Target found at index: {result_index}")
    print(f"Execution time (seconds): {elapsed_time:.6f}")
if __name__ == '__main__':
    run_benchmark()