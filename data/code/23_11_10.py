class RunLengthEncoder:
    @staticmethod
    def encode(data):
        if not data:
            return ""
        encoded = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = char
                count = 1
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

if __name__ == "__main__":
    sample = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoder = RunLengthEncoder()
    result = encoder.encode(sample)
    print(result)