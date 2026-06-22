class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        encoded_chars = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                encoded_chars.append(f"{count}{text[i - 1]}")
                count = 1
        encoded_chars.append(f"{count}{text[-1]}")
        return "".join(encoded_chars)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAAAABBBCCDEE"
    result = encoder.encode(sample_string)
    print(result)