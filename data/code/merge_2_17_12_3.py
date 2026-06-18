import time
def verify_element_existence(data: list, target) -> bool:
    for item in data:
        if item == target:
            return True
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_cases = [25, 99, 10]
    for target in test_cases:
        start_time = time.perf_counter()
        result = verify_element_existence(sample_data, target)
        end_time = time.perf_counter()
        print(f"Target {target}: Exists={result}, Time taken={(end_time - start_time)*10**6:.2f} microseconds")