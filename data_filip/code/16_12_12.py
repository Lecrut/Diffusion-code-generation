class RLEProcessor:
    SEPARATOR = ":"

    def encode(self, input_string):
        if not input_string:
            return []
        encoded_list = []
        char_index = 0
        length = len(input_string)
        while char_index < length:
            current_char = input_string[char_index]
            char_count = 0
            while char_index < length and input_string[char_index] == current_char:
                char_count += 1
                char_index += 1
            encoded_list.append((current_char, char_count))
        return encoded_list

if __name__ == '__main__':
    processor = RLEProcessor()
    result_a = processor.encode("AAABBC")
    print(result_a)
    result_b = processor.encode("")
    print(result_b)
    result_c = processor.encode("X")
    print(result_c)