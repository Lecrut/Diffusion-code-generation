def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    return hex(int(binary_string, 2))[2:]

if __name__ == '__main__':
    result = binary_to_hex('11111111')
    print(result)