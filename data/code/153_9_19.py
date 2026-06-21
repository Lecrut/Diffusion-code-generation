import time

def check_existence_in_list(item, data):
    return item in data

def check_existence_in_set(item, data):
    return item in data

if __name__ == '__main__':
    sample_item = 500000
    sample_data = list(range(1000000))
    sample_set_data = set(sample_data)

    start_time = time.time()
    check_existence_in_list(sample_item, sample_data)
    end_time = time.time()
    print(f"List check time: {end_time - start_time} seconds")

    start_time = time.time()
    check_existence_in_set(sample_item, sample_set_data)
    end_time = time.time()
    print(f"Set check time: {end_time - start_time} seconds")