class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(text))

if __name__ == '__main__':
    try:
        reverser = StringReverser()
        sample_values = ["Hello, World!", "Python is great.", "!dlroW ,olleH", 12345, None]
        for value in sample_values:
            try:
                result = reverser.reverse(value)
                print(f"Original: {value}, Reversed: {result}")
            except ValueError as e:
                print(f"Error reversing {value}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")