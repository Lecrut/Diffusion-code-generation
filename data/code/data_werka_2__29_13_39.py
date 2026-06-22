def reverse_string(s):
    return ''.join(reversed(s))

class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    def get_reversed(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "number": "12345",
        "word": "Python"
    }
    for key, value in sample_values.items():
        reverser = StringReverser(value)
        print(f"Original: {value} -> Reversed: {reverser.get_reversed()}")