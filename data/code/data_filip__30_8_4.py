import multiprocessing
from multiprocessing import Pool
import os

def decimal_to_binary(decimal_value):
    return bin(decimal_value)[2:]

def process_chunk(chunk):
    return [decimal_to_binary(val) for val in chunk]

def convert_decimals_to_binary_concurrent(decimals, num_processes=None):
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    if not decimals:
        return []
    
    chunk_size = len(decimals) // num_processes
    chunks = []
    for i in range(num_processes):
        start_idx = i * chunk_size
        if i == num_processes - 1:
            end_idx = len(decimals)
        else:
            end_idx = start_idx + chunk_size
        chunks.append(decimals[start_idx:end_idx])
    
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    flat_results = []
    for result in results:
        flat_results.extend(result)
    
    return flat_results

if __name__ == '__main__':
    sample_decimals = [0, 1, 2, 5, 10, 255, 1024, 2048, 4096, 8192, 65535, 131071, 999999, 123456789]
    binary_results = convert_decimals_to_binary_concurrent(sample_decimals)
    for dec, bin_str in zip(sample_decimals, binary_results):
        print(f"{dec} -> {bin_str}")