def decimal_to_binary(decimals):
    return [bin(n)[2:] for n in decimals]

if __name__ == '__main__':
    sample_decimals = [0, 5, 10, 255, 1024]
    print(decimal_to_binary(sample_decimals))