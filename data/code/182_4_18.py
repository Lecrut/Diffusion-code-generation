def unpack_string(s):
    return tuple(s)

if __name__ == '__main__':
    test_string_1 = "hello"
    result_1 = unpack_string(test_string_1)
    print(f"Input: '{test_string_1}', Output: {result_1}")
    
    test_string_2 = ""
    result_2 = unpack_string(test_string_2)
    print(f"Input: '{test_string_2}', Output: {result_2}")
    
    test_string_3 = "Python"
    result_3 = unpack_string(test_string_3)
    print(f"Input: '{test_string_3}', Output: {result_3}")