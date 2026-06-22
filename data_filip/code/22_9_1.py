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
                result.append(f"{count}{text[i - 1]}")
                count = 1
        result.append(f"{count}{text[-1]}")
        return "".join(result)

    def decode(self, text):
        if not text:
            return ""
        result = []
        i = 0
        while i < len(text):
            count = 0
            while i < len(text) and text[i].isdigit():
                count = count * 10 + int(text[i])
                i += 1
            if i < len(text):
                result.append(text[i] * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAABBBCCDAA"
    encoded = encoder.encode(original)
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)