import time
LARGE_DATASET_SIZE = 10000000
SAMPLE_ITEM = 1000000

def check_existence_in_list(item, data):
    return item in data

def check_existence_in_set(item, data):
    return item in data
if __name__ == '__main__':
    large_dataset = set(range(LARGE_DATASET_SIZE))
    start_time = time.time()
    check_existence_in_list(SAMPLE_ITEM, list(large_dataset))
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')
    start_time = time.time()
    check_existence_in_set(SAMPLE_ITEM, large_dataset)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')