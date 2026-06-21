class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(s[i - 1] + str(count))
                count = 1
        result.append(s[-1] + str(count))
        return "".join(result)

    def decode(self, s):
        if not s:
            return ""
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            i += 1
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            count = int(num_str)
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "AAABBBCCCA"
    encoded = encoder.encode(sample_input)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)