import timeit
def check_item_existence(data_list: list, target_value) -> bool:
    return target_value in data_list
if __name__ == '__main__':
    large_dataset = [i for i in range(10_000)]
    test_values = [5000, 9999, -1]
    results = []
    start_time = timeit.default_timer()
    for val in test_values:
        check_item_existence(large_dataset, val)
    end_time = timeit.default_timer()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    if 5000 in large_dataset and 9999 not in large_dataset:
        print("Validation Passed.")