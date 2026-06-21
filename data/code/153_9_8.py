import time

def check_existence_in_list(item, data):
    return item in data

def check_existence_in_set(item, data):
    return item in data

if __name__ == '__main__':
    sample_item = 500000
    large_dataset_list = list(range(1000000))
    large_dataset_set = set(range(1000000))

    start_time = time.time()
    result_list = check_existence_in_list(sample_item, large_dataset_list)
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')
    print(f'Item in list: {result_list}')

    start_time = time.time()
    result_set = check_existence_in_set(sample_item, large_dataset_set)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')
    print(f'Item in set: {result_set}')