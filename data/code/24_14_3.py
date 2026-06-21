class RunLengthEncoder:
    def __init__(self):
        self._buffer = []

    def _group_consecutive(self, data):
        if not data:
            return []
        groups = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                groups.append((count, current_char))
                current_char = char
                count = 1
        groups.append((count, current_char))
        return groups

    def encode(self, data):
        if not data:
            return ""
        groups = self._group_consecutive(data)
        self._buffer = [f"{count}{char}" for count, char in groups]
        return "".join(self._buffer)

    def decode(self, encoded_data):
        if not encoded_data:
            return ""
        result = []
        count_str = ""
        for char in encoded_data:
            if char.isdigit():
                count_str += char
            else:
                count = int(count_str)
                result.append(char * count)
                count_str = ""
        return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)