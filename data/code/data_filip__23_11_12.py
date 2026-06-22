class RunLengthEncoder:
    def __init__(self):
        self.cache = {}

    def encode(self, text: str) -> str:
        if not text:
            return ""
        if text in self.cache:
            return self.cache[text]
        encoded = []
        prev_char = text[0]
        count = 1
        for i in range(1, len(text)):
            char = text[i]
            if char == prev_char:
                count += 1
            else:
                encoded.append(f"{count}{prev_char}")
                prev_char = char
                count = 1
        encoded.append(f"{count}{prev_char}")
        result = "".join(encoded)
        self.cache[text] = result
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_text = "AAABBBCCDAA"
    result = encoder.encode(sample_text)
    print(result)