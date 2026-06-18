import time
def verify_element_existence(data: list, target) -> bool:
    for item in data:
        if item == target:
            return True
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_cases = [
        (sample_data, 45),
        (sample_data, 99),
        ([], 1)
    ]
    for dataset, element in test_cases:
        start_time = time.perf_counter()
        result = verify_element_existence(dataset, element)
        end_time = time.perf_counter()
        print(f"Element {element} exists in {dataset}: {result}")