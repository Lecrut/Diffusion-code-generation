def decimals_to_binaries(numbers):
    return [bin(n)[2:] for n in numbers]

if __name__ == '__main__':
    sample_values = [0, 1, 2, 10, 255, -5, -1]
    result = decimals_to_binaries(sample_values)
    print(result)