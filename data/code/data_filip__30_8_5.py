import multiprocessing
import sys

def _convert_single(value):
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")
    if value < 0:
        raise ValueError("Negative integers are not supported")
    if value == 0:
        return "0"
    binary_str = ""
    temp = value
    while temp > 0:
        binary_str = str(temp % 2) + binary_str
        temp //= 2
    return binary_str

def convert_decimal_to_binary_parallel(numbers):
    if not numbers:
        return []
    with multiprocessing.Pool() as pool:
        results = pool.map(_convert_single, numbers)
    return results

if __name__ == '__main__':
    sys.setrecursionlimit(1000)
    sample_data = [0, 1, 2, 3, 4, 5, 8, 15, 16, 255, 1024, 4096]
    output = convert_decimal_to_binary_parallel(sample_data)
    for original, converted in zip(sample_data, output):
        print(f"{original} -> {converted}")