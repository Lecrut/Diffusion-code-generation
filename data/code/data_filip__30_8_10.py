import multiprocessing
import itertools

def convert_single_decimal(args):
    number, bits = args
    return bin(number)[2:].zfill(bits)

def convert_decimals_to_binary(numbers, bits=8, processes=None):
    if processes is None:
        processes = max(1, multiprocessing.cpu_count())
    with multiprocessing.Pool(processes=processes) as pool:
        results = list(pool.map(convert_single_decimal, [(n, bits) for n in numbers]))
    return results

if __name__ == '__main__':
    sample_inputs = [0, 1, 2, 5, 10, 15, 127, 255, 1024, 2048, 4096, 8192, 16384, 32768, 65535]
    binary_strings = convert_decimals_to_binary(sample_inputs, bits=16)
    print(binary_strings)