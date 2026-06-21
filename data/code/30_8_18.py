import multiprocessing
import sys
from concurrent.futures import ProcessPoolExecutor

def decimal_to_binary(n):
    if n < 0:
        return bin(n)[1:]
    return bin(n)[2:]

def convert_batch(numbers):
    return [decimal_to_binary(n) for n in numbers]

def parallel_convert(numbers, chunk_size=1000):
    if not numbers:
        return []
    num_processes = min(multiprocessing.cpu_count(), len(numbers))
    results = []
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        batches = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
        for batch_result in executor.map(convert_batch, batches):
            results.extend(batch_result)
    return results

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 15, 128, 255, 1024, 4095, 65535, 131071, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727]
    result = parallel_convert(sample_values)
    for value, binary in zip(sample_values, result):
        print(f"{value} -> {binary}")