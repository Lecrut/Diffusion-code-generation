class RunLengthEncoder:
    def __init__(self):
        self.encoding_map = {}

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

    def decode(self, encoded_s):
        if not encoded_s:
            return ""

        result = []
        i = 0
        while i < len(encoded_s):
            count_str = ""
            while i < len(encoded_s) and encoded_s[i].isdigit():
                count_str += encoded_s[i]
                i += 1

            if i < len(encoded_s):
                char = encoded_s[i]
                i += 1
                count = int(count_str) if count_str else 1
                result.append(char * count)

        return "".join(result)

    def is_compressed(self, s, encoded_s):
        return len(encoded_s) < len(s)

    def encode_optimized(self, s):
        if not s:
            return s

        encoded = self.encode(s)
        if self.is_compressed(s, encoded):
            return encoded
        return s

if __name__ == "__main__":
    encoder = RunLengthEncoder()

    test_cases = [
        "",
        "a",
        "aa",
        "aaa",
        "aabcccccaaa",
        "abcd",
        "aabbc",
        "aabbccdd",
        "aaaaaaaaaa",
        "abcabcabc",
        "hello",
        "hhlloo",
        "wwwwwwwwwwwww",
        "w3",
        "111222333",
        "a1b2c3",
    ]

    for test in test_cases:
        encoded = encoder.encode(test)
        decoded = encoder.decode(encoded)
        optimized = encoder.encode_optimized(test)
        print(f"Input: '{test}' -> Encoded: '{encoded}' -> Decoded: '{decoded}' -> Optimized: '{optimized}'")