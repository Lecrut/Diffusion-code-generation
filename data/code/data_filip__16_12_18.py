class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return []
        result = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = text[i]
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbbcccd"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    empty_result = encoder.encode("")
    print(empty_result)
    single_result = encoder.encode("z")
    print(single_result)