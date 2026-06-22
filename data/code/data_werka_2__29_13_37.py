def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def get_reversed(self):
        return reverse_string(self.input_string)
    
    def is_palindrome(self):
        return self.input_string == self.get_reversed()

if __name__ == '__main__':
    sample_values = [
        "radar",
        "hello",
        "level"
    ]
    for value in sample_values:
        manipulator = StringManipulator(value)
        print(f"Original: {value} -> Reversed: {manipulator.get_reversed()}, Is Palindrome: {manipulator.is_palindrome()}")