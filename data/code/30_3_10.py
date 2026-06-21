def convert_integer_to_binary(number):
    if number == 0:
        return '0'
    
    is_neg = number < 0
    if is_neg:
        number = -number
    
    binary_digits = []
    while number > 0:
        remainder = number & 1
        if remainder:
            binary_digits.append('1')
        else:
            binary_digits.append('0')
        number >>= 1
    
    binary_digits.reverse()
    result_string = ''.join(binary_digits)
    
    if is_neg:
        return '-' + result_string
    
    return result_string

class BinaryConverter:
    def __init__(self):
        self.conversion_count = 0
    
    def convert(self, value):
        self.conversion_count += 1
        return convert_integer_to_binary(value)
    
    def get_count(self):
        return self.conversion_count

if __name__ == '__main__':
    converter_instance = BinaryConverter()
    test_values = [0, 1, -1, 10, 255, 1024, 65535, 1000000, -999999, 12345678901234567890]
    
    for val in test_values:
        binary_result = converter_instance.convert(val)
        print(binary_result)
    
    print(converter_instance.get_count())