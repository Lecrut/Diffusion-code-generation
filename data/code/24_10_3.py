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
                encoded.append(str(count))
                encoded.append(current_char)
                current_char = text[i]
                count = 1
        encoded.append(str(count))
        encoded.append(current_char)
        return "".join(encoded)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_text):
            num_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                num_str += encoded_text[i]
                i += 1
            if i < len(encoded_text):
                char = encoded_text[i]
                decoded.append(char * int(num_str))
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample1 = "AAAAABBBCCDAA"
    compressed1 = encoder.encode(sample1)
    decompressed1 = encoder.decode(compressed1)
    print(compressed1)
    print(decompressed1)
    sample2 = "A"
    compressed2 = encoder.encode(sample2)
    decompressed2 = encoder.decode(compressed2)
    print(compressed2)
    print(decompressed2)
    sample3 = "AAABBBCCD"
    compressed3 = encoder.encode(sample3)
    decompressed3 = encoder.decode(compressed3)
    print(compressed3)
    print(decompressed3)
    sample4 = ""
    compressed4 = encoder.encode(sample4)
    decompressed4 = encoder.decode(compressed4)
    print(compressed4)
    print(decompressed4)