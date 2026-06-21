def decimal_to_binary(n):
    return format(n, 'b')

if __name__ == '__main__':
    sample_integer = 42
    result = decimal_to_binary(sample_integer)
    print(result)