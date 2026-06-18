import time
def find_unique_items(item_names):
    result = {}
    for item in item_names:
        result[item] = True
    return result
if __name__ == '__main__':
    sample_names = ["apple", "banana", "apple", "orange", "banana", "grape"]
    start_time = time.perf_counter()
    unique_dict = find_unique_items(sample_names)
    end_time = time.perf_counter()
    print(unique_dict)