import json

class RLEEncoder:
    def __init__(self):
        self.sample_string = "aaabbc"

    def encode(self, text):
        if not text:
            return []

        result = []
        i = 0
        length = len(text)

        while i < length:
            current_char = text[i]
            count = 1
            while i + count < length and text[i + count] == current_char:
                count += 1
            result.append({'char': current_char, 'count': count})
            i += count
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    encoded = encoder.encode(encoder.sample_string)
    print(json.dumps(encoded))