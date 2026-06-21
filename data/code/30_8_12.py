import multiprocessing

def decimal_to_binary_chunk(chunk):
    return [bin(x)[2:] for x in chunk]

def convert_decimals_to_binary(numbers):
    if not numbers:
        return []
    chunk_size = max(1, len(numbers) // multiprocessing.cpu_count())
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    with multiprocessing.Pool() as pool:
        results = pool.map(decimal_to_binary_chunk, chunks)
    return [bit for sublist in results for bit in sublist]

if __name__ == '__main__':
    sample_inputs = [10, 255, 42, 0, 1, 1024, 7, 15, 31, 63]
    result = convert_decimals_to_binary(sample_inputs)
    print(result)