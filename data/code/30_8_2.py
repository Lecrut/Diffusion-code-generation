import multiprocessing
import os

def decimal_to_binary(n):
    if n < 0:
        return '-' + bin(-n)[2:]
    if n == 0:
        return '0'
    return bin(n)[2:]

def convert_batch(args):
    numbers, results, index = args
    for i, n in enumerate(numbers):
        results[index + i] = decimal_to_binary(n)

def convert_decimals_to_binary(numbers, pool_size=None):
    if pool_size is None:
        pool_size = multiprocessing.cpu_count()
    
    if not numbers:
        return []
    
    results = [None] * len(numbers)
    chunk_size = max(1, len(numbers) // pool_size)
    processes = []
    
    start_idx = 0
    while start_idx < len(numbers):
        end_idx = min(start_idx + chunk_size, len(numbers))
        chunk = numbers[start_idx:end_idx]
        p = multiprocessing.Process(
            target=convert_batch,
            args=(chunk, results, start_idx)
        )
        processes.append(p)
        p.start()
        start_idx = end_idx
    
    for p in processes:
        p.join()
    
    return results

if __name__ == '__main__':
    sample_decimals = [0, 1, 2, 10, 255, 1024, -5, 999999, 2**31 - 1, 2**63]
    binary_results = convert_decimals_to_binary(sample_decimals)
    print(binary_results)