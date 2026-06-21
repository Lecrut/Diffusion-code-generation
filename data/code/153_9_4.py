import time

def check_existence(data_structure):
    if isinstance(data_structure, set):
        return lambda item: item in data_structure
    elif isinstance(data_structure, list):
        return lambda item: item in data_structure
    else:
        raise ValueError("Unsupported data structure")

if __name__ == '__main__':
    sample_item = 500000
    large_dataset_set = set(range(1000000))
    large_dataset_list = list(large_dataset_set)

    check_set = check_existence(large_dataset_set)
    check_list = check_existence(large_dataset_list)

    start_time = time.time()
    for _ in range(10):
        check_set(sample_item)
    end_time = time.time()
    print(f'Set check time: {end_time - start_time} seconds')

    start_time = time.time()
    for _ in range(10):
        check_list(sample_item)
    end_time = time.time()
    print(f'List check time: {end_time - start_time} seconds')