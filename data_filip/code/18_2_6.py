class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = char
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode("AABCCC"))
    print(encoder.encode("ABCDE"))
    print(encoder.encode("AAAA"))
    print(encoder.encode(""))
    print(encoder.encode("XYZZZZ"))