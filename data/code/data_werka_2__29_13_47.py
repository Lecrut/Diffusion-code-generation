def reverse_string(s):
    return ''.join(reversed(s))

class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string
    def reverse(self):
        return reverse_string(self.input_string)

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    manipulator = StringManipulator(sample_text)
    reversed_text = manipulator.reverse()
    print(f"Original: {sample_text} -> Reversed: {reversed_text}")