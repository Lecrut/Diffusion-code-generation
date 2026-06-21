class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(str(count) + text[i - 1])
                count = 1
        result.append(str(count) + text[-1])
        return "".join(result)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        result = []
        i = 0
        while i < len(encoded_text):
            count_str = []
            while i < len(encoded_text) and encoded_text[i].isdigit():
                count_str.append(encoded_text[i])
                i += 1
            count = int("".join(count_str))
            char = encoded_text[i]
            result.append(char * count)
            i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original_text = "AAAABBBCCDAA"
    encoded = encoder.encode(original_text)
    decoded = encoder.decode(encoded)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")