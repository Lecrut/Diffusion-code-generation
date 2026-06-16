from typing import List, Any
def verify_element_existence(data: List[Any], target: Any) -> bool:
    return target in data
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_target_1 = 30
    test_target_2 = 99
    result_a = verify_element_existence(sample_data, test_target_1)
    print(f"Element {test_target_1} exists: {result_a}")
    result_b = verify_element_existence(sample_data, test_target_2)
    print(f"Element {test_target_2} exists: {result_b}")