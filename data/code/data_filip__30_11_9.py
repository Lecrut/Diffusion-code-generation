def decimal_to_binary(number):
    if number < 0:
        return '-' + decimal_to_binary(-number)
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result

if __name__ == '__main__':
    sample_values = [42, 0, 255, -10, 1]
    for value in sample_values:
        binary_string = decimal_to_binary(value)
        print('{}'.format(binary_string))