def decimal_to_binary_string(number):
    return "{:b}".format(number)

if __name__ == '__main__':
    sample_value = 42
    result = decimal_to_binary_string(sample_value)
    print(result)