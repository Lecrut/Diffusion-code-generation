class RLE:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        result = []
        current_char = self.data[0]
        count = 1
        for i in range(1, len(self.data)):
            char = self.data[i]
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    rle = RLE("aaabbc")
    print(rle.encode())