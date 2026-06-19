class StringManipulator:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(reversed(self.text))

    def is_palindrome(self):
        return self.text == self.reverse()

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    manipulator = StringManipulator(sample_string)
    reversed_string = manipulator.reverse()
    print(reversed_string)
    print(manipulator.is_palindrome())