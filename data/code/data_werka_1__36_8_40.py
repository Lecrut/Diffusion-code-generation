class StringProcessor:
    REVERSE_METHOD = 'slice'
    
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        if StringProcessor.REVERSE_METHOD == 'slice':
            return s[::-1]
        elif StringProcessor.REVERSE_METHOD == 'loop':
            reversed_str = ''
            for char in s:
                reversed_str = char + reversed_str
            return reversed_str
        else:
            raise ValueError("Unknown reverse method")

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        processor = StringProcessor()
        reversed_string = processor.reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)