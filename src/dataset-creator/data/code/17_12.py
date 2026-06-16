import time
def verify_element_existence(data_set: list, target_value) -> bool:
    return target_value in data_set
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_cases = [75, 45, -99]
    for value in test_cases:
        start_time = time.perf_counter()
        result = verify_element_existence(sample_data, value)
        end_time = time.perf_counter()
        print(f"Searching for {value}: {'Found' if result else 'Not Found'}")