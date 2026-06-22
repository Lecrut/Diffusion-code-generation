class RunLengthCompressor:
    def __init__(self, data):
        self.data = data

    def compress(self):
        if not self.data:
            return {}
        counts = {}
        current = self.data[0]
        total = 1
        index = 1
        length = len(self.data)
        while index < length:
            char = self.data[index]
            if char == current:
                total += 1
                index += 1
            else:
                counts[current] = total
                current = char
                total = 1
                index += 1
        counts[current] = total
        return counts

if __name__ == '__main__':
    compressor = RunLengthCompressor('AAABBC')
    print(compressor.compress())