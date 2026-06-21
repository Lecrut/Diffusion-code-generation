class RunLengthCoder:
    def encode(self, input_string):
        if not input_string:
            return ""
        result = []
        char_counter = 1
        current_symbol = input_string[0]
        string_length = len(input_string)
        index = 1
        while index < string_length:
            next_symbol = input_string[index]
            if next_symbol == current_symbol:
                char_counter += 1
            else:
                result.append(str(char_counter))
                result.append(current_symbol)
                current_symbol = next_symbol
                char_counter = 1
            index += 1
        result.append(str(char_counter))
        result.append(current_symbol)
        return "".join(result)

    def decode(self, compressed_string):
        if not compressed_string:
            return ""
        original_characters = []
        current_count_string = ""
        for char in compressed_string:
            if char.isdigit():
                current_count_string += char
            else:
                count = int(current_count_string)
                for _ in range(count):
                    original_characters.append(char)
                current_count_string = ""
        return "".join(original_characters)

if __name__ == '__main__':
    encoder = RunLengthCoder()
    original_text = "aabcccccaaa"
    compressed = encoder.encode(original_text)
    print(compressed)
    decoded_text = encoder.decode(compressed)
    print(decoded_text)