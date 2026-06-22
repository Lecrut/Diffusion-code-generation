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
                if count > 1:
                    result.append(str(count))
                result.append(current_char)
                current_char = char
                count = 1

        if count > 1:
            result.append(str(count))
        result.append(current_char)

        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbcdd"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    sample_input2 = "hello"
    encoded_result2 = encoder.encode(sample_input2)
    print(encoded_result2)
    sample_input3 = "a"
    encoded_result3 = encoder.encode(sample_input3)
    print(encoded_result3)
    sample_input4 = ""
    encoded_result4 = encoder.encode(sample_input4)
    print(encoded_result4)
    sample_input5 = "aa"
    encoded_result5 = encoder.encode(sample_input5)
    print(encoded_result5)
    sample_input6 = "aabbbcccc"
    encoded_result6 = encoder.encode(sample_input6)
    print(encoded_result6)