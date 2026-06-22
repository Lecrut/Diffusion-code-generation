class StringReverser:
    def __init__(self):
        self.reversed_text = ""

    def reverse(self, text):
        self.reversed_text = ''.join(reversed(text))
        return self.reversed_text

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "Python is great.", "!dlroW ,olleH", "12345", "racecar"]
    reverser = StringReverser()
    for test_input in sample_strings:
        print(f"Original String: '{test_input}'")
        reversed_output = reverser.reverse(test_input)
        print("Reversed String:", reversed_output)