class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        result = []
        count = 1
        length = len(text)
        for i in range(length):
            if i + 1 < length and text[i] == text[i + 1]:
                count += 1
            else:
                result.append(f"{count}{text[i]}")
                count = 1
        return "".join(result)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_string)
    print(encoded_result)