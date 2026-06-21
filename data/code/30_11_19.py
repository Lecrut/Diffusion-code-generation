def decimal_to_binary(n):
    return "{0:b}".format(n)

if __name__ == '__main__':
    decimal_value = 10
    binary_result = decimal_to_binary(decimal_value)
    print(binary_result)