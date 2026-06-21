import time

def check_existence_in_list(data, item):
    return item in data

def check_existence_in_set(data, item):
    return item in data

if __name__ == '__main__':
    sample_data = list(range(1000000))
    sample_item = 500000
    sample_set = set(sample_data)

    start_time = time.time()
    check_existence_in_list(sample_data, sample_item)
    end_time = time.time()
    print(f"List check time: {end_time - start_time} seconds")

    start_time = time.time()
    check_existence_in_set(sample_set, sample_item)
    end_time = time.time()
    print(f"Set check time: {end_time - start_time} seconds")