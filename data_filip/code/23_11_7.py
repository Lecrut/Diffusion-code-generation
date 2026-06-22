class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(f"{count}{text[i - 1]}")
                count = 1
        result.append(f"{count}{text[-1]}")
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_string = "aaabbbccca"
    encoded = encoder.encode(sample_string)
    print(encoded)