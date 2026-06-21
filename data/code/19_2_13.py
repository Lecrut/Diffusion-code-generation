class RunLengthEncoder:
    MAX_RUN_LENGTH = 1000

    def __init__(self):
        self.max_run = self.MAX_RUN_LENGTH

    def _encode_run(self, char, count):
        return f"{count}{char}"

    def compress(self, data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        run_length = 1
        total_chars = len(data)
        i = 1
        while i < total_chars:
            char = data[i]
            if char == current_char and run_length < self.max_run:
                run_length += 1
            else:
                result.append(self._encode_run(current_char, run_length))
                current_char = char
                run_length = 1
            i += 1
        result.append(self._encode_run(current_char, run_length))
        return "".join(result)

    def decompress(self, compressed_data):
        if not compressed_data:
            return ""
        result = []
        i = 0
        length = len(compressed_data)
        while i < length:
            if not compressed_data[i].isdigit():
                raise ValueError(f"Invalid compressed data format at index {i}")
            num_start = i
            while i < length and compressed_data[i].isdigit():
                i += 1
            count_str = compressed_data[num_start:i]
            count = int(count_str)
            if i >= length:
                raise ValueError("Unexpected end of data while reading character")
            char = compressed_data[i]
            i += 1
            result.append(char * count)
        return "".join(result)

if __name__ == "__main__":
    sample_input = "AAAAABBBCCCCCCCCCCDDDDD"
    compressor = RunLengthEncoder()
    compressed_output = compressor.compress(sample_input)
    decompressed_output = compressor.decompress(compressed_output)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed_output}")
    print(f"Decompressed: {decompressed_output}")
    is_match = sample_input == decompressed_output
    print(f"Roundtrip successful: {is_match}")