class RLEIterator:
    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError("Data must be a string")
        self.data = data
        self.index = 0
        self.current_char = None
        self.current_count = 0
        self.length = len(data)
        self._advance()

    def _advance(self):
        self.current_char = None
        self.current_count = 0
        if self.index < self.length:
            self.current_char = self.data[self.index]
            char = self.current_char
            count = 0
            i = self.index
            while i < self.length and self.data[i] == char:
                count += 1
                i += 1
            self.current_count = count
            self.index = i

    def next_char(self):
        if self.current_count > 0:
            self.current_count -= 1
            return self.current_char
        if self.index < self.length:
            self._advance()
            if self.current_count > 0:
                self.current_count -= 1
                return self.current_char
        return None

    def __iter__(self):
        return self

    def __next__(self):
        char = self.next_char()
        if char is None:
            raise StopIteration
        return char

class RLECompressor:
    def compress(self, data):
        if not isinstance(data, str) or len(data) == 0:
            return data
        result = []
        iterator = iter(data)
        char = next(iterator)
        count = 1
        for c in iterator:
            if c == char:
                count += 1
            else:
                result.append(char)
                result.append(str(count))
                char = c
                count = 1
        result.append(char)
        result.append(str(count))
        return ''.join(result)

    def decompress(self, compressed_data):
        if not isinstance(compressed_data, str) or len(compressed_data) == 0:
            return compressed_data
        result = []
        i = 0
        length = len(compressed_data)
        while i < length:
            char = compressed_data[i]
            i += 1
            if i < length:
                num_str = ''
                while i < length and compressed_data[i].isdigit():
                    num_str += compressed_data[i]
                    i += 1
                if len(num_str) > 0:
                    count = int(num_str)
                    result.append(char * count)
            else:
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    compressor = RLECompressor()
    compressed = compressor.compress(sample_string)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)