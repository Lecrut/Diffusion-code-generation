def decimal_to_binary(number):
    return "{0:b}".format(number)

if __name__ == '__main__':
    sample_value = 42
    result = decimal_to_binary(sample_value)
    print(result)