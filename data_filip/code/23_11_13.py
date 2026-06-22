class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        result = []
        count = 1
        current_char = text[0]
        for index in range(1, len(text)):
            if text[index] == current_char:
                count += 1
            else:
                result.append(f"{current_char}{count}")
                current_char = text[index]
                count = 1
        result.append(f"{current_char}{count}")
        return "".join(result)

if __name__ == "__main__":
    sample_input = "AAAABBBCCDAAA"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)