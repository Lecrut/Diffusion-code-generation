class StringReverser:
    REVERSE_SLICE = slice(None, None, -1)
    
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s[StringReverser.REVERSE_SLICE]
    
if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = StringReverser.reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)