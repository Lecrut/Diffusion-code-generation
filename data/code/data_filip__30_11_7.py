def decimal_to_binary(decimal_int):
    return format(decimal_int, 'b')

if __name__ == '__main__':
    decimal_value = 42
    result = decimal_to_binary(decimal_value)
    print(result)