class StringReverser:
    def reverse(self, text):
        reversed_text = ''.join([text[i] for i in range(len(text)-1, -1, -1)])
        return reversed_text

if __name__ == '__main__':
    sample_values = {
        "hello world": "dlrow olleh",
        "Python is great.": ".taerg si nohtyP",
        "!dlroW ,olleH": "Hello, World!"
    }
    
    reverser = StringReverser()
    for original, expected in sample_values.items():
        result = reverser.reverse(original)
        print(f"Original: '{original}' | Reversed: '{result}' | Expected: '{expected}'")