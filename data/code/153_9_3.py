import time

def check_existence_in_list(item, data):
    return item in data

def check_existence_in_set(item, data):
    return item in data
if __name__ == '__main__':
    sample_item = 1000000
    large_dataset = set(range(10000000))
    start_time = time.time()
    check_existence_in_list(sample_item, list(large_dataset))
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')
    start_time = time.time()
    check_existence_in_set(sample_item, large_dataset)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')