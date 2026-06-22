def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_chars = []
    while n > 0:
        remainder = n % 2
        binary_chars.append(str(remainder))
        n = n // 2
    
    binary_chars.reverse()
    return "".join(binary_chars)

if __name__ == '__main__':
    test_value_1 = 10
    test_value_2 = 255
    test_value_3 = 0
    test_value_4 = 1
    test_value_5 = 13
    
    result_1 = decimal_to_binary(test_value_1)
    result_2 = decimal_to_binary(test_value_2)
    result_3 = decimal_to_binary(test_value_3)
    result_4 = decimal_to_binary(test_value_4)
    result_5 = decimal_to_binary(test_value_5)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)