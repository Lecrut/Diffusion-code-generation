class RunLengthEncoding:
    def encode(self, text):
        if not text:
            return ""
        encoded = []
        char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == char:
                count += 1
            else:
                encoded.append(f"{count}{char}")
                char = text[i]
                count = 1
        encoded.append(f"{count}{char}")
        return "".join(encoded)

    def decode(self, encoded):
        if not encoded:
            return ""
        decoded = []
        current_num = []
        for char in encoded:
            if char.isdigit():
                current_num.append(char)
            else:
                count = int("".join(current_num))
                decoded.append(char * count)
                current_num = []
        return "".join(decoded)

if __name__ == '__main__':
    rle = RunLengthEncoding()
    original = "AAABBBCCC"
    encoded = rle.encode(original)
    print(encoded)
    decoded = rle.decode(encoded)
    print(decoded)