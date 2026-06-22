def decimal_to_binary(decimal_value):
    if decimal_value < 0:
        return "-" + format(abs(decimal_value), 'b')
    return format(decimal_value, 'b')

if __name__ == '__main__':
    number = 42
    result = decimal_to_binary(number)
    print(result)