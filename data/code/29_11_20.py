class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        encoded = []
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = char
                count = 1
        encoded.append(str(count) + current_char)
        return "".join(encoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode(""))
    print(encoder.encode("a"))
    print(encoder.encode("aaa"))
    print(encoder.encode("aabbccc"))
    print(encoder.encode("aabbbcccc"))
    print(encoder.encode("abcde"))
    print(encoder.encode("aabbccddeeff"))