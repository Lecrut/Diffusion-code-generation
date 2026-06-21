import multiprocessing
import os

def convert_decimal_to_binary(number):
    try:
        return f"{number}:{bin(number)[2:]}"
    except Exception:
        return f"{number}:ERROR"

def process_batch(numbers):
    results = []
    with multiprocessing.Pool() as pool:
        results = pool.map(convert_decimal_to_binary, numbers)
    return results

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 100, 255, 1024, 4096, 65535]
    output = process_batch(sample_numbers)
    for line in output:
        print(line)