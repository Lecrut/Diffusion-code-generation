def run_length_encode_efficient(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    iterator = iter(data)
    next(iterator, None)
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            yield (count, current_char)
            current_char = char
            count = 1
    yield (count, current_char)

class RLEProcessor:
    def __init__(self, text):
        self.text = text

    def encode(self):
        return list(run_length_encode_efficient(self.text))

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    processor = RLEProcessor(sample_text)
    print(processor.encode())