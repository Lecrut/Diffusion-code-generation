import multiprocessing
from typing import List

def decimal_to_binary_worker(n: int) -> str:
    if n < 0:
        raise ValueError("Only non-negative integers supported")
    return bin(n)[2:]

def convert_decimals_to_binaries_concurrent(numbers: List[int], processes: int = 4) -> List[str]:
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(decimal_to_binary_worker, numbers)
    return results

if __name__ == '__main__':
    sample_data = [10, 15, 255, 1024, 65535, 0, 1, 42, 7, 31337, 123456, 999999, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    output = convert_decimals_to_binaries_concurrent(sample_data)
    for original, binary in zip(sample_data, output):
        print(f"{original}: {binary}")