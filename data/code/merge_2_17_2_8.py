import timeit
def check_item_existence(data_list: list, target_value) -> bool:
    return target_value in data_list
if __name__ == '__main__':
    large_dataset = [i for i in range(10_000)]
    sample_values = {5000, 9999, -1}
    start_time = timeit.default_timer()
    result = check_item_existence(large_dataset, 5000)
    end_time = timeit.default_timer()
    print(f"Item exists: {result}")
    print(f"Execution time (single run): {end_time - start_time:.6f} seconds")