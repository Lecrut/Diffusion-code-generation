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

    def decode(self, s):
        if not s:
            return ""
        result = []
        i = 0
        while i < len(s):
            count = ""
            while i < len(s) and s[i].isdigit():
                count += s[i]
                i += 1
            if not count:
                break
            char = s[i]
            i += 1
            result.append(char * int(count))
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode(""))
    print(encoder.encode("a"))
    print(encoder.encode("aaabbbcc"))
    print(encoder.encode("aabbbcccc"))
    print(encoder.decode(""))
    print(encoder.decode("1a"))
    print(encoder.decode("3a3b2c"))
    print(encoder.decode("2a3b4c"))