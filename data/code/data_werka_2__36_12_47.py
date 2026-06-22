class StringManipulator:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    for original in sample_sentences:
        result = StringManipulator.reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed: {result}")