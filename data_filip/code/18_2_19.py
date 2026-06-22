class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        result = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(str(count))
                result.append(current_char)
                current_char = text[i]
                count = 1
        result.append(str(count))
        result.append(current_char)
        return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbccccd"
    encoder = RunLengthEncoder()
    encoded_value = encoder.encode(sample_string)
    print(encoded_value)