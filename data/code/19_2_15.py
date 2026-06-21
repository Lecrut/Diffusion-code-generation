class RunLengthIterator:
    def __init__(self, compressed_data: str):
        self.compressed_data = compressed_data
        self.pos = 0
        self.data_len = len(compressed_data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= self.data_len:
            raise StopIteration
        count_str = ""
        while self.pos < self.data_len and self.compressed_data[self.pos].isdigit():
            count_str += self.compressed_data[self.pos]
            self.pos += 1
        if self.pos >= self.data_len:
            raise ValueError("Compressed data ends with a number")
        char = self.compressed_data[self.pos]
        self.pos += 1
        count = int(count_str)
        for _ in range(count):
            yield char

class RLEHandler:
    def compress(self, text: str) -> str:
        if not text:
            return ""
        result = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, compressed: str) -> str:
        if not compressed:
            return ""
        result = []
        iterator = RunLengthIterator(compressed)
        for char in iterator:
            result.append(char)
        return "".join(result)

if __name__ == '__main__':
    handler = RLEHandler()
    original = "AAAAAAAAABCCCCC"
    compressed = handler.compress(original)
    decompressed = handler.decompress(compressed)
    print(compressed)
    print(decompressed)