import time

def check_existence(item, data_structure):
    return item in data_structure

if __name__ == '__main__':
    sample_item = 500000
    large_dataset_list = list(range(1000000))
    large_dataset_set = set(range(1000000))

    start_time = time.time()
    check_existence(sample_item, large_dataset_list)
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')

    start_time = time.time()
    check_existence(sample_item, large_dataset_set)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')