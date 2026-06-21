class RLEProcessor:
    def __init__(self):
        self._buffer_size = 4096

    def _compress_chunk(self, data_iter):
        result = []
        try:
            current_char = next(data_iter)
        except StopIteration:
            return ""
        count = 1
        for char in data_iter:
            if char == current_char:
                count += 1
                if count >= 100:
                    result.append(f"{count}{current_char}")
                    current_char = char
                    count = 0
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def compress(self, data):
        if not isinstance(data, str):
            raise TypeError("Input must be a string")
        if not data:
            return ""
        data_iter = iter(data)
        result_parts = []
        while True:
            chunk = self._compress_chunk(data_iter)
            if not chunk:
                break
            result_parts.append(chunk)
        return "".join(result_parts)

    def _decompress_sequence(self, count_str, char):
        return char * count_str

    def decompress(self, data):
        if not isinstance(data, str):
            raise TypeError("Input must be a string")
        if not data:
            return ""
        result = []
        i = 0
        n = len(data)
        while i < n:
            count_start = i
            while i < n and data[i].isdigit():
                i += 1
            if i == count_start:
                raise ValueError("Invalid compressed format: missing count")
            count = int(data[count_start:i])
            if i >= n:
                raise ValueError("Invalid compressed format: missing character")
            char = data[i]
            i += 1
            result.append(char * count)
        return "".join(result)

if __name__ == "__main__":
    processor = RLEProcessor()
    original_text = "AAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJ"
    compressed = processor.compress(original_text)
    decompressed = processor.decompress(compressed)
    print(f"Original: {original_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original_text == decompressed}")