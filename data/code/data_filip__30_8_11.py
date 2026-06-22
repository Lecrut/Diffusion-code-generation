import multiprocessing

def decimal_to_binary(n):
    return bin(n)[2:] if n >= 0 else '-' + bin(abs(n))[2:]

def convert_batch(args):
    return list(map(decimal_to_binary, args[0]))

def convert_decimals_to_binary_concurrently(decimals, chunk_size=None):
    if not decimals:
        return []

    if chunk_size is None:
        chunk_size = max(1, len(decimals) // multiprocessing.cpu_count())

    chunks = []
    for i in range(0, len(decimals), chunk_size):
        chunks.append(decimals[i:i + chunk_size])

    with multiprocessing.Pool() as pool:
        results = pool.map(convert_batch, chunks)

    flat_results = []
    for chunk_result in results:
        flat_results.extend(chunk_result)

    return flat_results

if __name__ == '__main__':
    sample_decimals = [0, 1, 2, 10, 255, 1024, -5, -10, 0, 128, 256, 512, 1000000]
    binary_strings = convert_decimals_to_binary_concurrently(sample_decimals)
    for dec, b in zip(sample_decimals, binary_strings):
        print(f"{dec} -> {b}")