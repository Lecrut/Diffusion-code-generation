import multiprocessing
import os

def decimal_to_binary_worker(decimals):
    return [bin(d)[2:] for d in decimals]

def convert_decimals_to_binary_concurrent(decimals, num_workers=None):
    if num_workers is None:
        num_workers = multiprocessing.cpu_count()
    
    if not decimals:
        return []
    
    chunk_size = max(1, len(decimals) // num_workers)
    chunks = []
    for i in range(0, len(decimals), chunk_size):
        chunks.append(decimals[i:i + chunk_size])
    
    with multiprocessing.Pool(processes=num_workers) as pool:
        results = pool.map(decimal_to_binary_worker, chunks)
    
    flat_results = []
    for chunk_result in results:
        flat_results.extend(chunk_result)
    
    return flat_results

if __name__ == '__main__':
    sample_decimals = [0, 1, 2, 5, 10, 255, 1024, 2048, 4096, 8192]
    results = convert_decimals_to_binary_concurrent(sample_decimals)
    print(results)