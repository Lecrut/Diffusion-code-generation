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
                result.append(text[i - 1])
                if count > 1:
                    result.append(str(count))
                count = 1
        result.append(text[-1])
        if count > 1:
            result.append(str(count))
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_inputs = ["", "a", "aa", "aabbbcccc", "aabbccddeeff"]
    for s in sample_inputs:
        print(f"Input: '{s}' -> Encoded: '{encoder.encode(s)}'")