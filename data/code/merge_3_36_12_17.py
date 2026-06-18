class StringReverser:
    def reverse(self, text):
        """Returns a new string with the characters of 'text' in reverse order."""
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        "hello world",
        "",
        "A man, a plan, a canal: Panama!",
        "Python3"
    ]

    reverser = StringReverser()

    for original in test_cases:
        reversed_text = reverser.reverse(original)
        print(f'Original:  "{original}"')
        print(f'Reversed:  "{reversed_text}"')
        print("-" * 30)