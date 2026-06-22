class RLEIterator:
    def __init__(self, source_iter):
        self.source_iter = iter(source_iter)
        self.current_char = None
        self.count = 0
        self._fill()

    def _fill(self):
        count = 0
        current = self.current_char
        try:
            while True:
                char = next(self.source_iter)
                if char == current:
                    count += 1
                else:
                    break
            self.current_char = char
            self.count = count
        except StopIteration:
            if count > 0:
                self.current_char = current
                self.count = count
            else:
                self.current_char = None
                self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_char is None:
            raise StopIteration
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return self.current_char

class RunLengthEncoder:
    def encode(self, iterable):
        iterator = iter(iterable)
        try:
            prev = next(iterator)
        except StopIteration:
            return []
        
        current_char = prev
        current_count = 1
        result = []
        
        for char in iterator:
            if char == current_char:
                current_count += 1
            else:
                result.append((current_char, current_count))
                current_char = char
                current_count = 1
        
        result.append((current_char, current_count))
        return result

    def decode(self, encoded_list):
        buffer = []
        for char, count in encoded_list:
            buffer.extend([char] * count)
        return ''.join(buffer)

class RLEProcessor:
    def __init__(self):
        self.encoder = RunLengthEncoder()

    def compress(self, text):
        encoded = self.encoder.encode(text)
        return encoded

    def decompress(self, encoded):
        return self.encoder.decode(encoded)

if __name__ == '__main__':
    processor = RLEProcessor()
    
    sample_text = "AAABBBCCCDAA"
    compressed = processor.compress(sample_text)
    print(compressed)
    
    decompressed = processor.decompress(compressed)
    print(decompressed)