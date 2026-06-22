class RunLengthCodec:
    def encode(self, text):
        if not text:
            return ""
        result = []
        idx = 0
        length = len(text)
        while idx < length:
            current_char = text[idx]
            count = 1
            while idx + 1 < length and text[idx + 1] == current_char:
                count += 1
                idx += 1
            result.append(f"{count}{current_char}")
            idx += 1
        return "".join(result)

    def decode(self, text):
        if not text:
            return ""
        result = []
        idx = 0
        length = len(text)
        while idx < length:
            num_str = ""
            while idx < length and text[idx].isdigit():
                num_str += text[idx]
                idx += 1
            if idx >= length:
                break
            count = int(num_str)
            char = text[idx]
            result.append(char * count)
            idx += 1
        return "".join(result)

if __name__ == "__main__":
    codec = RunLengthCodec()
    original = "AAABBBCCCCDDDDD"
    encoded = codec.encode(original)
    decoded = codec.decode(encoded)
    print(encoded)
    print(decoded)