def decimal_to_binary(decimal_list):
    return [bin(n)[2:] for n in decimal_list]

if __name__ == '__main__':
    decimals = [0, 1, 10, 255, 1024]
    binary_strings = decimal_to_binary(decimals)
    print(binary_strings)