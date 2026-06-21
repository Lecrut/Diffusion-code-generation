import json

class RLEEncoder:
    def __init__(self):
        self.data = "aabcccccaaa"

    def encode(self):
        original = self.data
        encoded = []
        index = 0
        length = len(original)
        while index < length:
            current_char = original[index]
            count = 1
            while index + count < length and original[index + count] == current_char:
                count += 1
            encoded.append({
                'char': current_char,
                'count': count
            })
            index += count
        return json.dumps(encoded)

if __name__ == '__main__':
    encoder = RLEEncoder()
    print(encoder.encode())