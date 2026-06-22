import re
import zlib

class RLECompressor:
    def compress(self, data):
        if not isinstance(data, str):
            return None

        if not data:
            return ""

        compressed = ""
        current_char = data[0]
        count = 1

        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed += f"{count}{current_char}"
                current_char = char
                count = 1

        compressed += f"{count}{current_char}"
        return compressed

    def decompress(self, compressed_data):
        if not isinstance(compressed_data, str):
            return None

        if not compressed_data:
            return ""

        decompressed = ""
        pattern = re.compile(r"(\d+)(.)")
        matches = pattern.findall(compressed_data)

        if not matches:
            return compressed_data

        for count_str, char in matches:
            try:
                count = int(count_str)
                decompressed += char * count
            except ValueError:
                return compressed_data

        return decompressed

if __name__ == '__main__':
    compressor = RLECompressor()

    sample_string = "AAABBBCCCDDDD"
    compressed = compressor.compress(sample_string)
    print(compressed)

    decompressed = compressor.decompress(compressed)
    print(decompressed)

    empty_string = ""
    compressed_empty = compressor.compress(empty_string)
    print(compressed_empty)

    decompressed_empty = compressor.decompress(compressed_empty)
    print(decompressed_empty)

    single_char = "A"
    compressed_single = compressor.compress(single_char)
    print(compressed_single)

    decompressed_single = compressor.decompress(compressed_single)
    print(decompressed_single)

    mixed_string = "Hello World!!!"
    compressed_mixed = compressor.compress(mixed_string)
    print(compressed_mixed)

    decompressed_mixed = compressor.decompress(compressed_mixed)
    print(decompressed_mixed)

    invalid_input_compress = compressor.compress(12345)
    print(invalid_input_compress)

    invalid_input_decompress = compressor.decompress(None)
    print(invalid_input_decompress)

    malformed_compressed = compressor.decompress("abc123")
    print(malformed_compressed)

    numbers_string = "111222333"
    compressed_numbers = compressor.compress(numbers_string)
    print(compressed_numbers)

    decompressed_numbers = compressor.decompress(compressed_numbers)
    print(decompressed_numbers)