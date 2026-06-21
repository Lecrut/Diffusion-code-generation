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

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbcdddeeggh"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)

    empty_input = ""
    empty_result = encoder.encode(empty_input)
    print(repr(empty_result))

    single_char = "x"
    single_result = encoder.encode(single_char)
    print(single_result)

    mixed_input = "aabbcc"
    mixed_result = encoder.encode(mixed_input)
    print(mixed_result)