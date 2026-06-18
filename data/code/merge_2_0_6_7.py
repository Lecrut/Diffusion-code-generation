import time
from typing import List, Tuple
def check_value_matches(values: List[int]) -> bool:
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            match_equal = values[i] == values[j]
            match_is = values[i] is values[j]
            if not (match_equal and match_is):
                return False
    return True
def process_large_dataset(data_size: int) -> Tuple[int, float]:
    start_time = time.perf_counter()
    values = list(range(100)) * (data_size // 256 + 1)
    result = check_value_matches(values)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time
if __name__ == '__main__':
    test_values = [10, 20, 30, 40]
    print("Testing with small dataset:", check_value_matches(test_values))
    result, duration = process_large_dataset(500)
    print(f"Large scale test completed. Result: {result}, Time: {duration:.6f} seconds")