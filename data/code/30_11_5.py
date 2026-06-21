def decimal_to_binary_string(n):
    return format(n, 'b')

if __name__ == '__main__':
    decimal_integer = 42
    result = decimal_to_binary_string(decimal_integer)
    print(result)