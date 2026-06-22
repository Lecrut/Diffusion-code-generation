class RunLengthEncoder:
    def encode(self, s):
        if not s:
            return ""
        result = []
        count = 1
        current_char = s[0]
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = s[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decode(self, s):
        if not s:
            return ""
        result = []
        i = 0
        while i < len(s):
            count_str = ""
            while i < len(s) and s[i].isdigit():
                count_str += s[i]
                i += 1
            if i < len(s):
                count = int(count_str)
                char = s[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWWWW"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)