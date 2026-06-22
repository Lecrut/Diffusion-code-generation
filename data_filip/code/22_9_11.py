class RunLengthEncoding:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                encoded.append(f"{count}{text[i - 1]}")
                count = 1
        encoded.append(f"{count}{text[-1]}")
        return "".join(encoded)

    def decode(self, text: str) -> str:
        if not text:
            return ""
        decoded = []
        i = 0
        while i < len(text):
            if text[i].isdigit():
                count_str = ""
                while i < len(text) and text[i].isdigit():
                    count_str += text[i]
                    i += 1
                count = int(count_str)
                char = text[i]
                decoded.append(char * count)
                i += 1
            else:
                decoded.append(text[i])
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    rle = RunLengthEncoding()
    original = "AAABBBCCDAA"
    encoded = rle.encode(original)
    print(encoded)
    decoded = rle.decode(encoded)
    print(decoded)