import io
import sys

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

def run_length_encode(data):
    if not data:
        return ""
    parts = []
    for char, count in RLEIterator(data):
        parts.append(str(count))
        parts.append(char)
    return "".join(parts)

if __name__ == '__main__':
    sample = "AAABBBCCCCD"
    result = run_length_encode(sample)
    print(result)