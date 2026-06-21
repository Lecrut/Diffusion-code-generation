class RLEManager:
    def __init__(self):
        self.default_separator = ""

    def compress(self, data):
        if not isinstance(data, str):
            return str(data)
        if not data:
            return ""
        result_parts = []
        current_char = data[0]
        run_length = 1
        for index in range(1, len(data)):
            char = data[index]
            if char == current_char:
                run_length += 1
            else:
                result_parts.append(self._format_pair(current_char, run_length))
                current_char = char
                run_length = 1
        result_parts.append(self._format_pair(current_char, run_length))
        return "".join(result_parts)

    def decompress(self, data):
        if not isinstance(data, str):
            return str(data)
        if not data:
            return ""
        result_chars = []
        index = 0
        length = len(data)
        while index < length:
            if data[index].isdigit():
                start = index
                while index < length and data[index].isdigit():
                    index += 1
                count_str = data[start:index]
                count = int(count_str)
                if index < length:
                    char = data[index]
                    result_chars.append(char * count)
                    index += 1
                else:
                    return ""
            else:
                result_chars.append(data[index])
                index += 1
        return "".join(result_chars)

    def _format_pair(self, character, count):
        if count > 1:
            return str(count) + character
        return character

if __name__ == '__main__':
    manager = RLEManager()
    test_input_1 = "aaabbcddde"
    compressed_1 = manager.compress(test_input_1)
    print(compressed_1)
    decompressed_1 = manager.decompress(compressed_1)
    print(decompressed_1)
    test_input_2 = "hello world"
    compressed_2 = manager.compress(test_input_2)
    print(compressed_2)
    decompressed_2 = manager.decompress(compressed_2)
    print(decompressed_2)
    test_input_3 = ""
    compressed_3 = manager.compress(test_input_3)
    print(compressed_3)
    decompressed_3 = manager.decompress(compressed_3)
    print(decompressed_3)
    test_input_4 = "12333"
    compressed_4 = manager.compress(test_input_4)
    print(compressed_4)
    decompressed_4 = manager.decompress(compressed_4)
    print(decompressed_4)