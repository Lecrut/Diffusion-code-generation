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
        decoded = []
        i = 0
        while i < len(encoded_text):
            num_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                num_str += encoded_text[i]
                i += 1
            if i < len(encoded_text):
                char = encoded_text[i]
                count = int(num_str) if num_str else 1
                decoded.append(char * count)
                i += 1
        return "".join(decoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed = encoder.encode(original)
    restored = encoder.decode(compressed)
    print(compressed)
    print(restored)