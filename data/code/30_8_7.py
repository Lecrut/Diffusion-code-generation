import multiprocessing as mp
import struct

def decimal_to_binary_chunk(args):
    nums, start_idx = args
    results = []
    for num in nums:
        if num < 0:
            val = num + (1 << 32)
            bin_str = bin(val)[2:].zfill(32)
            bin_str = bin_str[7:8] + '1' + bin_str[9:]
            results.append(bin_str)
        else:
            if num == 0:
                results.append('0')
            else:
                bin_str = bin(num)[2:]
                results.append(bin_str)
    return start_idx, results

def convert_decimals_to_binary(decimals):
    if not decimals:
        return []
    chunk_size = max(1, len(decimals) // mp.cpu_count())
    chunks = []
    for i in range(0, len(decimals), chunk_size):
        chunk = decimals[i:i + chunk_size]
        chunks.append((chunk, i))
    with mp.Pool() as pool:
        results = pool.map(decimal_to_binary_chunk, chunks)
    sorted_results = sorted(results, key=lambda x: x[0])
    final_binary_strings = []
    for _, res_list in sorted_results:
        final_binary_strings.extend(res_list)
    return final_binary_strings

if __name__ == '__main__':
    sample_decimals = [0, 1, 5, 10, 255, 1024, -1, -5]
    binary_results = convert_decimals_to_binary(sample_decimals)
    print(binary_results)