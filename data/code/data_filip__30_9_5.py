def integer_to_binary_string(number: int) -> str:
    if number == 0:
        return '0'
    
    is_negative = number < 0
    if is_negative:
        number = -number
    
    bits = []
    while number > 0:
        remainder = number % 2
        bits.append(str(remainder))
        number = number // 2
    
    bits.reverse()
    result = ''.join(bits)
    
    if is_negative:
        result = '-' + result
    
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10, 255, 1024, 1337, -42, -1]
    for val in test_values:
        result = integer_to_binary_string(val)
        print(f"{val} -> {result}")