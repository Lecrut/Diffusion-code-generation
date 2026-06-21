class RunLengthEncoder:
    def __init__(self):
        self._separator = None

    def _flush_buffer(self, current_char: str, count: int, buffer: list) -> None:
        if current_char:
            buffer.append((current_char, count))

    def encode(self, text: str) -> list:
        if not text:
            return []
        
        encoded_list = []
        current_char = text[0]
        count = 1
        
        for index in range(1, len(text)):
            next_char = text[index]
            if next_char == current_char:
                count += 1
            else:
                self._flush_buffer(current_char, count, encoded_list)
                current_char = next_char
                count = 1
        
        self._flush_buffer(current_char, count, encoded_list)
        return encoded_list

    def encode_with_boundary_check(self, text: str) -> list:
        if not text:
            return []
        
        if len(text) == 1:
            return [(text[0], 1)]
        
        result = self.encode(text)
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_data = "aaabbccccd"
    encoded_result = encoder.encode(sample_data)
    print(encoded_result)
    single_char_result = encoder.encode("z")
    print(single_char_result)
    empty_result = encoder.encode("")
    print(empty_result)