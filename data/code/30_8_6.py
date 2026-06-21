import multiprocessing

def decimal_to_binary(value):
    return bin(value)[2:]

def convert_decimals_to_binaries(decimals):
    with multiprocessing.Pool() as pool:
        results = pool.map(decimal_to_binary, decimals)
    return results

if __name__ == '__main__':
    sample_decimals = [10, 255, 1024, 7, 0, 1, 128, 256, 512, 1023]
    binary_results = convert_decimals_to_binaries(sample_decimals)
    print(binary_results)