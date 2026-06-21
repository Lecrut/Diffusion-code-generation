class RLEIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.length = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        
        char = self.text[self.index]
        count = 1
        
        while self.index + 1 < self.length and self.text[self.index + 1] == char:
            count += 1
            self.index += 1
            
        self.index += 1
        yield (char, count)

class RLECompressor:
    def __init__(self, text):
        self.text = text

    def compress(self):
        iterator = RLEIterator(self.text)
        compressed = []
        for char, count in iterator:
            compressed.append(f"{count}{char}")
        return ''.join(compressed)

class RLEDecompressor:
    def __init__(self, compressed_text):
        self.compressed_text = compressed_text

    def decompress(self):
        iterator = RLEIterator(self.compressed_text)
        decompressed = []
        for char, count in iterator:
            decompressed.append(char * count)
        return ''.join(decompressed)

if __name__ == '__main__':
    original_string = "AAABBBCCCDAA"
    compressor = RLECompressor(original_string)
    compressed_result = compressor.compress()
    print(f"Compressed: {compressed_result}")
    
    decompressor = RLEDecompressor(compressed_result)
    decompressed_result = decompressor.decompress()
    print(f"Decompressed: {decompressed_result}")
    
    print(f"Match: {original_string == decompressed_result}")