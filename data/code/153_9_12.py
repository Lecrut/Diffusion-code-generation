import time

def check_existence_in_list(item, dataset):
    return item in dataset

def check_existence_in_set(item, dataset):
    return item in dataset

if __name__ == '__main__':
    sample_item = 1000000
    large_dataset = set(range(10000000))

    start_time = time.time()
    result_list = check_existence_in_list(sample_item, large_dataset)
    end_time = time.time()
    print(f"List check time: {end_time - start_time}")

    start_time = time.time()
    result_set = check_existence_in_set(sample_item, large_dataset)
    end_time = time.time()
    print(f"Set check time: {end_time - start_time}")