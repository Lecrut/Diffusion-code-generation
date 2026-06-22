def decimal_to_binary(decimal_value):
    return format(decimal_value, 'b')

if __name__ == '__main__':
    decimal_value = 10
    result = decimal_to_binary(decimal_value)
    print(result)