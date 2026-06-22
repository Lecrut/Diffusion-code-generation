class RLEIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.length = len(text)
        self.current_char = None
        self.current_count = 0
        self._advance()

    def _advance(self):
        if self.index >= self.length:
            self.current_char = None
            self.current_count = 0
            return
        char = self.text[self.index]
        count = 0
        while self.index < self.length and self.text[self.index] == char:
            count += 1
            self.index += 1
        self.current_char = char
        self.current_count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_char is None:
            raise StopIteration
        result = (self.current_char, self.current_count)
        self._advance()
        return result

class RLEProcessor:
    def __init__(self, text):
        self.text = text

    def compress(self):
        result = []
        iterator = RLEIterator(self.text)
        for char, count in iterator:
            if count > 1:
                result.append(str(count))
            result.append(char)
        return "".join(result)

    def decompress(self, compressed_text):
        result = []
        iterator = RLEIterator(compressed_text)
        for char, count in iterator:
            if count > 1:
                result.append(char * count)
            else:
                result.append(char)
        return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    processor = RLEProcessor(original)
    compressed = processor.compress()
    decompressed = processor.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original == decompressed}")