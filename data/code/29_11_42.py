def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

class StringProcessor:
    def __init__(self, text):
        self.text = text

    def process(self):
        reversed_text = reverse_string(self.text)
        return reversed_text

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Alibaba Cloud",
        "Python Programming"
    ]
    for original in sample_texts:
        processor = StringProcessor(original)
        result = processor.process()
        print(f"Original: {original}, Reversed: {result}")