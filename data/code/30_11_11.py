def decimal_to_binary(n):
    return "{0:b}".format(n)

if __name__ == '__main__':
    number = 42
    result = decimal_to_binary(number)
    print(result)