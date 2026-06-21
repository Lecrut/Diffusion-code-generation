class RunLengthEncoder:
    def __init__(self, min_run_length: int = 1):
        if min_run_length < 1:
            raise ValueError("Minimum run length must be at least 1")
        self.min_run_length = min_run_length

    def _process_sequence(self, char: str, count: int, output: list) -> None:
        if count >= self.min_run_length:
            output.append((char, count))
        else:
            for _ in range(count):
                output.append((char, 1))

    def encode(self, text: str) -> list[tuple[str, int]]:
        if not text:
            return []
        result = []
        current_char = text[0]
        count = 1
        for index in range(1, len(text)):
            next_char = text[index]
            if next_char == current_char:
                count += 1
            else:
                self._process_sequence(current_char, count, result)
                current_char = next_char
                count = 1
        self._process_sequence(current_char, count, result)
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder(min_run_length=2)
    sample_input = "AABBBCCCCDEEEE"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    empty_result = encoder.encode("")
    print(empty_result)
    single_result = encoder.encode("Z")
    print(single_result)