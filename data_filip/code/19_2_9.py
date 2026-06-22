class RLEIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0
        self._length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._length:
            raise StopIteration
        current_char = self._data[self._index]
        count = 1
        while self._index + count < self._length and self._data[self._index + count] == current_char:
            count += 1
        self._index += count
        return (current_char, count)

class RLECompressor:
    def __init__(self):
        self._encoded = []

    def encode_string(self, data):
        iterator = RLEIterator(data)
        self._encoded = []
        for char, count in iterator:
            self._encoded.append((char, count))
        return self._encoded

    def decode_string(self):
        result = []
        for char, count in self._encoded:
            result.append(char * count)
        return ''.join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    source_data = "AAAAABBBCCDEEEE"
    encoded_result = compressor.encode_string(source_data)
    print(encoded_result)
    decoded_result = compressor.decode_string()
    print(decoded_result)