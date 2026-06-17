import timeit
class PrintIndexProcessor:
    def __init__(self):
        self.data = [10, 25, 30, 45, 60]
    def find_target_index(self, target_value=45):
        start_time = timeit.default_timer()
        for index in range(len(self.data)):
            if self.data[index] == target_value:
                return index
        end_time = timeit.default_timer()
        print(f"Target {target_value} not found.")
        return -1
def run_processor():
    processor = PrintIndexProcessor()
    test_targets = [45, 60, 25]
    results = []
    for target in test_targets:
        index = processor.find_target_index(target)
        if index != -1:
            print(f"Target {target} found at index {index}")
if __name__ == '__main__':
    run_processor()