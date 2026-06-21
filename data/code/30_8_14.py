import multiprocessing
import itertools

def decimal_to_binary(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return bin(number)[2:]

def convert_decimals_to_binary(decimal_list):
    cpu_count = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=cpu_count) as pool:
        binary_results = pool.map(decimal_to_binary, decimal_list)
    return binary_results

if __name__ == '__main__':
    sample_decimals = [
        0, 1, 2, 3, 4, 10, 15, 16, 100, 255, 256,
        1024, 4096, 65535, 65536, 100000, 1000000,
        10000000, 100000000, 1000000000, 2147483647,
        4294967295, 9223372036854775807
    ]
    binary_strings = convert_decimals_to_binary(sample_decimals)
    print(binary_strings)