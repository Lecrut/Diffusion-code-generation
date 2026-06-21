def decimal_to_binary(decimal_list):
    return [bin(n)[2:] if n >= 0 else '-' + bin(n)[3:] for n in decimal_list]

if __name__ == '__main__':
    sample_numbers = [0, 1, 5, 10, 255, -5]
    result = decimal_to_binary(sample_numbers)
    print(result)