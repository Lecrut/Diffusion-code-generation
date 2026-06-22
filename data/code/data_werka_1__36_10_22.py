class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text[::-1]

if __name__ == '__main__':
    try:
        reverser = StringReverser()
        sample_values = ["Hello, World!", "Python is great.", "!dlroW ,olleH", 12345]
        for value in sample_values:
            print(reverser.reverse(value))
    except ValueError as e:
        print(e)