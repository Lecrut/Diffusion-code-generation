import time
def create_item_list(input_list):
    return list(input_list)
if __name__ == '__main__':
    sample_input = ["apple", "banana", "cherry", "date", "elderberry"]
    start_time = time.perf_counter()
    result = create_item_list(sample_input)
    end_time = time.perf_counter()
    print(result)
    print(f"Execution time: {end_time - start_time}")