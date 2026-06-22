class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""

        result = []
        current_char = text[0]
        count = 1

        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1

        result.append(f"{count}{current_char}")
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCDAA"
    encoded_result = encoder.encode(sample_string)
    print(encoded_result)