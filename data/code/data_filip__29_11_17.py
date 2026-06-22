class RLEEncoder:
    def encode(self, s):
        if not s:
            return ""
        if len(s) == 1:
            return s

        result = []
        current_char = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(f"{current_char}{count}")
                current_char = s[i]
                count = 1
        result.append(f"{current_char}{count}")
        return "".join(result)

if __name__ == '__main__':
    encoder = RLEEncoder()
    test_cases = ["", "a", "aaabbbcc", "aabbcc", "wwwwaaadexxxxxx"]
    for t in test_cases:
        print(f"{repr(t)} -> {encoder.encode(t)}")