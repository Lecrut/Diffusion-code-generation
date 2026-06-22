class RLECodec:
    def __init__(self, separator=""):
        self.separator = separator

    def encode(self, data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return self.separator.join(result)

    def decode(self, encoded_data):
        if not encoded_data:
            return ""
        result = []
        count_str = []
        for char in encoded_data:
            if char.isdigit():
                count_str.append(char)
            else:
                count = int("".join(count_str))
                result.append(char * count)
                count_str = []
        return "".join(result)

if __name__ == '__main__':
    codec = RLECodec()
    sample_text = "AAAABBBCCDAA"
    encoded_result = codec.encode(sample_text)
    print(encoded_result)
    decoded_result = codec.decode(encoded_result)
    print(decoded_result)
    empty_sample = ""
    empty_encoded = codec.encode(empty_sample)
    print(empty_encoded)