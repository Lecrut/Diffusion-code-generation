class RleEncoder:
    def __init__(self, source: str):
        self.source = source

    def encode(self) -> str:
        if not self.source:
            return ""
        result = []
        current = self.source[0]
        count = 1
        for char in self.source[1:]:
            if char == current:
                count += 1
            else:
                result.append(f"{count}{current}")
                current = char
                count = 1
        result.append(f"{count}{current}")
        return "".join(result)

def run_length_encode(input_string: str) -> str:
    encoder = RleEncoder(input_string)
    return encoder.encode()

if __name__ == "__main__":
    sample_data = "AAAABBBCCD"
    encoder_instance = RleEncoder(sample_data)
    print(run_length_encode(sample_data))
    print(encoder_instance.encode())