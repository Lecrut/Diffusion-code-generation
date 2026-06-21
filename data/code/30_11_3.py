def decimal_to_binary(decimal_number):
    return format(decimal_number, 'b')

if __name__ == '__main__':
    sample_decimal = 42
    binary_result = decimal_to_binary(sample_decimal)
    print(binary_result)