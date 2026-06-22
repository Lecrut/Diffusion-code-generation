import json
import collections

class RLEEncoder:
    def __init__(self):
        self.sample_string = "AAABBBCCDAA"

    def encode(self, text=None):
        if text is None:
            text = self.sample_string

        if not text:
            return []

        encoded = []
        i = 0
        n = len(text)

        while i < n:
            char = text[i]
            count = 1
            while i + count < n and text[i + count] == char:
                count += 1
            encoded.append({"char": char, "count": count})
            i += count

        return encoded

if __name__ == '__main__':
    encoder = RLEEncoder()
    result = encoder.encode()
    print(json.dumps(result))