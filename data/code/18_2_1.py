class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        current_char = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(str(count))
                result.append(current_char)
                current_char = s[i]
                count = 1
        result.append(str(count))
        result.append(current_char)
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_input = "aaabbccccd"
    output = encoder.encode(sample_input)
    print(output)