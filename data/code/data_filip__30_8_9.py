import multiprocessing
import math

def decimal_to_binary(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number == 0:
        return "0"
    negative = number < 0
    number = abs(number)
    bits = []
    while number > 0:
        bits.append(str(number % 2))
        number //= 2
    result = "".join(reversed(bits))
    if negative:
        return "-" + result
    return result

def convert_decimals_to_binaries(decimals):
    with multiprocessing.Pool() as pool:
        results = pool.map(decimal_to_binary, decimals)
    return results

if __name__ == '__main__':
    sample_decimals = [0, 1, -1, 10, -10, 100, -100, 255, -255, 1024, -1024, 1000000, -1000000]
    binary_results = convert_decimals_to_binaries(sample_decimals)
    print(binary_results)