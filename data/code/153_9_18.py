import time

def check_existence(data_structure, item):
    return item in data_structure

if __name__ == '__main__':
    sample_list = list(range(10**6))
    sample_set = set(sample_list)
    item_to_check = 5 * 10**5

    start_time = time.time()
    result_list = check_existence(sample_list, item_to_check)
    end_time = time.time()
    print(f"List check time: {end_time - start_time} seconds")

    start_time = time.time()
    result_set = check_existence(sample_set, item_to_check)
    end_time = time.time()
    print(f"Set check time: {end_time - start_time} seconds")