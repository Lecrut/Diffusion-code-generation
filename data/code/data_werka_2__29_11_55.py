class StringManipulator:
    def __init__(self, text):
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
        result = manipulator.reverse()
        print(f"Original: {original}, Reversed: {result}")