class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_text = "Hello, World!"
    reversed_text = reverser.reverse(sample_text)
    print(reversed_text)