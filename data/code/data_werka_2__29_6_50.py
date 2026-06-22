class StringReverser:
    def __init__(self):
        self.SUPPORTED_TYPES = (str,)
    
    def reverse_string(self, input_string):
        if not isinstance(input_string, self.SUPPORTED_TYPES):
            raise ValueError("Input must be a string")
        return ''.join(reversed(input_string))

if __name__ == '__main__':
    SAMPLE_VALUES = [
        "hello",
        "world",
        "Python",
        "12345",
        "!@#$%",
        12345,
        None
    ]
    
    reverser = StringReverser()
    for value in SAMPLE_VALUES:
        try:
            print(reverser.reverse_string(value))
        except ValueError as e:
            print(e)