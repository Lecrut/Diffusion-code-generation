import time
def create_item_list(string_list):
    return sorted(string_list)
if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "date", "elderberry"]
    start_time = time.perf_counter()
    sorted_list = create_item_list(sample_data)
    end_time = time.perf_counter()
    print(sorted_list)