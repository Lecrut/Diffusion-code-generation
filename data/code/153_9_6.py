import time

def check_existence_in_list(item, data):
    return item in data

def check_existence_in_set(item, data):
    return item in data

if __name__ == '__main__':
    sample_item = 10**6
    sample_data = set(range(10**7))
    
    start_time = time.time()
    result_list = check_existence_in_list(sample_item, list(sample_data))
    end_time = time.time()
    print(f"List check time: {end_time - start_time} seconds")
    
    start_time = time.time()
    result_set = check_existence_in_set(sample_item, sample_data)
    end_time = time.time()
    print(f"Set check time: {end_time - start_time} seconds")