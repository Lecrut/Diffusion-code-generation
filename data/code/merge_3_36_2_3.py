class StringReverser:
    def reverse(self, text):
        """Reverse a given string without modifying it in place."""
        return ''.join(reversed(text))

if __name__ == '__main__':
    sample_text = "Hello, World!"
    reverser = StringReverser()
    reversed_result = reverser.reverse(sample_text)

    print(f"Original: {sample_text}")
    print(f"Reversed:{reversed_result}")