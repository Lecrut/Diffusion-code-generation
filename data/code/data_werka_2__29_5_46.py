class TextProcessor:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def reverse(self):
        return self.text[::-1]

    def is_palindrome(self):
        return self.text == self.reverse()

if __name__ == '__main__':
    sample_text = "civic"
    processor = TextProcessor(sample_text)
    reversed_text = processor.reverse()
    palindrome_check = processor.is_palindrome()
    print(reversed_text)
    print(palindrome_check)