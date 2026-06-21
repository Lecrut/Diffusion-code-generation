def decimal_to_binary_list(decimals):
    return [bin(n)[2:] for n in decimals]

if __name__ == '__main__':
    sample_decimals = [0, 1, 2, 5, 10, 255, -3, -10]
    print(decimal_to_binary_list(sample_decimals))