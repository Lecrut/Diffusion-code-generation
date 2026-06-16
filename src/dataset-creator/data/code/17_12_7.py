import time
def verify_element_existence(data: list, target) -> bool:
    return target in data
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_target_1 = 30
    test_target_2 = 99
    start_time = time.time()
    result_existence = verify_element_existence(sample_data, test_target_1)
    end_time = time.time()
    print(f"Element {test_target_1} exists: {result_existence}")
    if not result_existence:
        raise ValueError("Verification failed for expected element.")
    start_time = time.time()
    verify_element_existence(sample_data, test_target_2)
    end_time = time.time()
    print(f"Element {test_target_2} exists: False")