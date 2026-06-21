class RLEncoder:
    def __init__(self, text):
        self.text = text

    def encode(self):
        if not self.text:
            return []
        result = []
        iterator = iter(self.text)
        current_char = next(iterator)
        count = 1
        for char in iterator:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    sample_data = 'AAAABBBCCDAA'
    encoder = RLEncoder(sample_data)
    print(encoder.encode())