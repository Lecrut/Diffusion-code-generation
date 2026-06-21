class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return []
        if len(data) == 1:
            return [(data[0], 1)]
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = data[i]
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "aaabbcdddd"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    empty_input = ""
    empty_result = encoder.encode(empty_input)
    print(empty_result)
    single_input = "x"
    single_result = encoder.encode(single_input)
    print(single_result)