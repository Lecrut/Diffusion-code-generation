import time
def verify_element_existence(data: list, target: any) -> bool:
    return target in data
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    test_cases = [30, 99, 25]
    for item in test_cases:
        result = verify_element_existence(sample_data, item)
        print(f"Element {item} exists: {result}")