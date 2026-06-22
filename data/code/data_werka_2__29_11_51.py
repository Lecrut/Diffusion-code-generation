class StringManipulator:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def reverse(self):
        return self.text[::-1]

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Alibaba Cloud",
        "Python Programming"
    ]
    
    for original in sample_texts:
        manipulator = StringManipulator(original)
        reversed_text = manipulator.reverse()
        print(f"Original: {original}, Reversed: {reversed_text}")