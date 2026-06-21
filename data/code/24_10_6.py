class RunLengthEncoding:
    def __init__(self):
        self.history = []

    def encode(self, source):
        if not source:
            return ""
        result_parts = []
        previous_char = source[0]
        run_length = 1
        for current_char in source[1:]:
            if current_char == previous_char:
                run_length += 1
            else:
                result_parts.append(f"{run_length}{previous_char}")
                previous_char = current_char
                run_length = 1
        result_parts.append(f"{run_length}{previous_char}")
        final_string = "".join(result_parts)
        self.history.append(("encoded", final_string))
        return final_string

    def decode(self, compressed_data):
        if not compressed_data:
            return ""
        decoded_parts = []
        index = 0
        length = len(compressed_data)
        while index < length:
            count_str = []
            while index < length and compressed_data[index].isdigit():
                count_str.append(compressed_data[index])
                index += 1
            if not count_str:
                break
            count = int("".join(count_str))
            if index < length:
                char = compressed_data[index]
                decoded_parts.append(char * count)
                index += 1
            else:
                break
        final_result = "".join(decoded_parts)
        self.history.append(("decoded", final_result))
        return final_result

    def get_history(self):
        return list(self.history)

if __name__ == '__main__':
    rle_processor = RunLengthEncoding()
    test_input_1 = "AAAABBBCCDAA"
    test_input_2 = "XYZ"
    test_input_3 = ""
    
    compressed_1 = rle_processor.encode(test_input_1)
    decompressed_1 = rle_processor.decode(compressed_1)
    
    compressed_2 = rle_processor.encode(test_input_2)
    decompressed_2 = rle_processor.decode(compressed_2)
    
    compressed_3 = rle_processor.encode(test_input_3)
    decompressed_3 = rle_processor.decode(compressed_3)
    
    print(compressed_1)
    print(decompressed_1)
    print(compressed_2)
    print(decompressed_2)
    print(compressed_3)
    print(decompressed_3)
    print(rle_processor.get_history())