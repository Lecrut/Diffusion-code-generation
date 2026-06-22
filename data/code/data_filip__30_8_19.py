import multiprocessing
import os

def decimal_to_binary(n):
    if n < 0:
        return '-' + bin(abs(n))[2:]
    return bin(n)[2:]

def convert_decimals_to_binaries(decimals):
    binary_results = []
    with multiprocessing.Pool() as pool:
        binary_results = pool.map(decimal_to_binary, decimals)
    return binary_results

if __name__ == '__main__':
    sample_decimals = [10, 255, 0, 1024, -42, 123456789]
    binary_strings = convert_decimals_to_binaries(sample_decimals)
    print(binary_strings)