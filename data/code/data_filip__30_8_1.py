import multiprocessing
import os

def decimal_to_binary(dec: int) -> str:
    if dec == 0:
        return '0'
    negative = dec < 0
    dec = abs(dec)
    bits = []
    while dec > 0:
        bits.append(str(dec % 2))
        dec //= 2
    result = ''.join(reversed(bits))
    if negative:
        result = '-' + result
    return result

def _worker_batch(input_list: list) -> list:
    results = []
    for num in input_list:
        results.append(decimal_to_binary(num))
    return results

def convert_decimals_to_binary(numbers: list) -> list:
    if not numbers:
        return []
    chunk_size = max(1, len(numbers) // (multiprocessing.cpu_count() * 2))
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    with multiprocessing.Pool() as pool:
        partial_results = pool.map(_worker_batch, chunks)
    final_results = []
    for part in partial_results:
        final_results.extend(part)
    return final_results
if __name__ == '__main__':
    sample_numbers = [10, 255, 0, -1, 1024, 1, 65535, 123456789]
    binary_strings = convert_decimals_to_binary(sample_numbers)
    print(binary_strings)