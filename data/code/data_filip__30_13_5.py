def decimal_to_binary(n):
    return bin(n)[2:]

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))