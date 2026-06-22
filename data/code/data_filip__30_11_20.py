def decimal_to_binary(n):
    return format(n, 'b')

if __name__ == '__main__':
    decimal_value = 42
    result = decimal_to_binary(decimal_value)
    print(result)