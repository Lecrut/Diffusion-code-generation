def convert_to_binary(decimals):
    return [bin(n)[2:] for n in decimals]

if __name__ == '__main__':
    sample_values = [0, 5, 10, 255, 1024]
    result = convert_to_binary(sample_values)
    print(result)