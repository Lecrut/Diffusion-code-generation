import multiprocessing
from typing import List

def _decimal_to_binary_worker(num: int) -> int:
    return bin(num)[2:]

def convert_decimals_to_binary_concurrent(numbers: List[int]) -> List[str]:
    with multiprocessing.Pool() as pool:
        results = pool.map(_decimal_to_binary_worker, numbers)
    return results

if __name__ == '__main__':
    sample_data = [1, 2, 5, 10, 15, 16, 100, 255, 1024, 4096]
    binary_results = convert_decimals_to_binary_concurrent(sample_data)
    for original, binary in zip(sample_data, binary_results):
        print(f"Decimal: {original} -> Binary: {binary}")