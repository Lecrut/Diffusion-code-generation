class StringReverser:
    def reverse(self, text):
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text
        return reversed_text

if __name__ == '__main__':
    reverser = StringReverser()
    sample_strings = {
        "hello": "olleh",
        "world": "dlrow",
        "Python": "nohtyP"
    }
    
    for original, expected in sample_strings.items():
        reversed_string = reverser.reverse(original)
        print(f"Original: {original}, Reversed: {reversed_string}")