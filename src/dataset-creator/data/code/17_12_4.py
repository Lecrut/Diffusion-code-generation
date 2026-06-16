import time
def verify_element_existence(data: list, target) -> bool:
    for item in data:
        if item == target:
            return True
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_target = 45
    start_time = time.perf_counter()
    result = verify_element_existence(sample_data, test_target)
    end_time = time.perf_counter()
    print(f"Element {test_target} exists: {result}")