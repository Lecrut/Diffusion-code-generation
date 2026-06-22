class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        encoded = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_text):
            num_str = []
            while i < len(encoded_text) and encoded_text[i].isdigit():
                num_str.append(encoded_text[i])
                i += 1
            count = int("".join(num_str))
            char = encoded_text[i]
            i += 1
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original_string = "aaabbc"
    encoded_string = encoder.encode(original_string)
    decoded_string = encoder.decode(encoded_string)
    print(f"Original: {original_string}")
    print(f"Encoded: {encoded_string}")
    print(f"Decoded: {decoded_string}")
    print(f"Match: {original_string == decoded_string}")