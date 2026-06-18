import time
def create_item_list(string_list):
    unique_items = set(string_list)
    result_list = list(unique_items)
    return result_list
if __name__ == '__main__':
    sample_input = ["apple", "banana", "apple", "orange", "banana", "grape"]
    start_time = time.perf_counter()
    unique_result = create_item_list(sample_input)
    end_time = time.perf_counter()
    print(unique_result)