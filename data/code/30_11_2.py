def decimal_to_binary(decimal_value):
    if decimal_value < 0:
        return '-' + format(-decimal_value, 'b')
    return format(decimal_value, 'b')

if __name__ == '__main__':
    sample_values = [42, 0, -15, 255, 1024]
    for value in sample_values:
        result = decimal_to_binary(value)
        print(result)