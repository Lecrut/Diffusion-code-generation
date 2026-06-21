def decimal_to_binary(decimal_list):
    return [bin(num)[2:] for num in decimal_list]

if __name__ == '__main__':
    sample_decimals = [0, 1, 10, 255, 1024]
    result = decimal_to_binary(sample_decimals)
    print(result)