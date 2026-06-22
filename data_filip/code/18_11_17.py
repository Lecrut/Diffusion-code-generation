class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = char
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    @staticmethod
    def decompress(data):
        if not data:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            if not data[i].isdigit():
                raise ValueError("Invalid format: expected digit")
            j = i
            while j < len(data) and data[j].isdigit():
                j += 1
            count = int(data[i:j])
            if j >= len(data):
                raise ValueError("Invalid format: missing character")
            char = data[j]
            decompressed.append(char * count)
            i = j + 1
        return "".join(decompressed)

    @staticmethod
    def run_tests():
        test_cases = [
            ("AAABBBCCCC", "3A3B4C"),
            ("AAAAA", "5A"),
            ("", ""),
            ("A", "1A"),
            ("XYZ", "1X1Y1Z"),
            ("123", "1123"),
            ("11A22B", "11A22B"),
        ]
        for input_val, expected in test_cases:
            compressed = RunLengthEncoder.compress(input_val)
            assert compressed == expected, f"Compression failed for {input_val}: got {compressed}, expected {expected}"
            if input_val:
                decompressed = RunLengthEncoder.decompress(compressed)
                assert decompressed == input_val, f"Decompression failed for {compressed}: got {decompressed}, expected {input_val}"

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "AAABBCCCCDD"
    compressed_output = encoder.compress(sample_input)
    decompressed_output = encoder.decompress(compressed_output)
    print(compressed_output)
    print(decompressed_output)
    encoder.run_tests()