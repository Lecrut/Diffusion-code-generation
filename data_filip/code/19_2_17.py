class RLEIterator:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        char = self.data[self.index]
        count = 1
        while self.index + count < self.length and self.data[self.index + count] == char:
            count += 1
        self.index += count
        return (char, count)

class RunLengthEncoder:
    def __init__(self):
        self.compressed = []

    def encode(self, data):
        iterator = RLEIterator(data)
        self.compressed = []
        for char, count in iterator:
            self.compressed.append((char, count))
        return self.compressed

    def decode(self, data):
        result = []
        for char, count in data:
            result.append(char * count)
        return ''.join(result)

def run_sample():
    encoder = RunLengthEncoder()
    sample_data = "AAAAABBBCCDEEEE"
    compressed = encoder.encode(sample_data)
    decoded = encoder.decode(compressed)
    print(compressed)
    print(decoded)

if __name__ == '__main__':
    run_sample()