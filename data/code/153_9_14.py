import time

class DatasetChecker:
    def __init__(self, dataset_size):
        self.dataset = set(range(dataset_size))

    def check_existence_in_list(self, item):
        return item in list(self.dataset)

    def check_existence_in_set(self, item):
        return item in self.dataset

if __name__ == '__main__':
    checker = DatasetChecker(1000000)
    sample_item = 500000
    start_time = time.time()
    result_list = checker.check_existence_in_list(sample_item)
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')
    start_time = time.time()
    result_set = checker.check_existence_in_set(sample_item)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')
    print(f'Item in list: {result_list}')
    print(f'Item in set: {result_set}')