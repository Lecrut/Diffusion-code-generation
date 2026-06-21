class RunLengthEncoder:
    def encode(self, s: str) -> str:
        if not s:
            return ""
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(f"{count}{s[i - 1]}")
                count = 1
        result.append(f"{count}{s[-1]}")
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    test_cases = ["", "a", "aabbbbcccd", "WWWWWWWWWWWWB"]
    for case in test_cases:
        print(f"Input: '{case}' -> Encoded: {encoder.encode(case)}")