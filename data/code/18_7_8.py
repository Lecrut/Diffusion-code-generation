class RunLengthEncoder:
    def __init__(self, min_run_length):
        self.min_run_length = min_run_length

    def _format_run(self, character, count):
        if count >= self.min_run_length:
            return str(count) + character
        return character * count

    def encode(self, data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        length = len(data)
        index = 1
        while index < length:
            char = data[index]
            if char == current_char:
                count += 1
            else:
                result.append(self._format_run(current_char, count))
                current_char = char
                count = 1
            index += 1
        result.append(self._format_run(current_char, count))
        return "".join(result)

if __name__ == "__main__":
    sample_string = "AAABBBCCCCCCCCDDDD"
    encoder = RunLengthEncoder(2)
    encoded_value = encoder.encode(sample_string)
    print(encoded_value)