def run_length_encode_iterative(input_string):
    if not input_string:
        return ""
    result_parts = []
    iterator = iter(input_string)
    try:
        current_char = next(iterator)
    except StopIteration:
        return ""
    count = 1
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result_parts.append(str(count))
            result_parts.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result_parts.append(str(count))
    result_parts.append(current_char)
    return "".join(result_parts)

def run_length_decode_iterative(encoded_string):
    if not encoded_string:
        return ""
    result_chars = []
    iterator = iter(encoded_string)
    current_digit_buffer = ""
    try:
        for char in iterator:
            if char.isdigit():
                current_digit_buffer += char
            else:
                count = int(current_digit_buffer) if current_digit_buffer else 1
                result_chars.append(char * count)
                current_digit_buffer = ""
    except ValueError:
        return ""
    return "".join(result_chars)

class RLEProcessor:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def encode(self):
        return run_length_encode_iterative(self.input_data)
    
    def decode(self):
        return run_length_decode_iterative(self.input_data)

if __name__ == '__main__':
    sample_input = "aaabbbccccdddddeeeefff"
    processor = RLEProcessor(sample_input)
    encoded_value = processor.encode()
    print(encoded_value)
    decoded_value = processor.decode()
    print(decoded_value)
    
    test_string_2 = "zzz"
    processor_2 = RLEProcessor(test_string_2)
    print(processor_2.encode())
    
    test_string_3 = "a"
    processor_3 = RLEProcessor(test_string_3)
    print(processor_3.encode())
    
    test_string_4 = "1234567890"
    processor_4 = RLEProcessor(test_string_4)
    print(processor_4.encode())