def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_reversed(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    sample_data = {
        "greeting": "Hello, World!",
        "numeric": "12345",
        "word": "Python"
    }
    
    for description, value in sample_data.items():
        manipulator = StringManipulator(value)
        print(f"Original ({description}): {value} -> Reversed: {manipulator.get_reversed()}")