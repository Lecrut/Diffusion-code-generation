import multiprocessing

def decimal_to_binary_chunk(chunk):
    results = []
    for num in chunk:
        results.append(bin(num)[2:])
    return results

def convert_decimals_to_binary_parallel(decimals, chunk_size=100):
    if not decimals:
        return []
    
    chunks = [decimals[i:i + chunk_size] for i in range(0, len(decimals), chunk_size)]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(decimal_to_binary_chunk, chunks)
    
    return [bit_string for sublist in results for bit_string in sublist]

if __name__ == '__main__':
    sample_decimals = [10, 15, 255, 1024, 0, 1, 42, 100, 200, 300, 512, 1023]
    binary_strings = convert_decimals_to_binary_parallel(sample_decimals)
    print(binary_strings)