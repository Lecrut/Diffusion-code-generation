def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

class StringProcessor:
    def __init__(self, text):
        self.text = text

    def get_reversed_text(self):
        return reverse_string(self.text)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Alibaba Cloud",
        "Python Programming"
    ]
    
    for original in sample_texts:
        processor = StringProcessor(original)
        reversed_text = processor.get_reversed_text()
        print(f"Original: {original}, Reversed: {reversed_text}")