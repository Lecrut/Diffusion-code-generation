class StringReverser:
    REVERSE_SLICE = slice(None, None, -1)
    
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s[StringReverser.REVERSE_SLICE]
    
if __name__ == '__main__':
    sample_sentences = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    for original in sample_sentences:
        try:
            result = StringReverser.reverse_string(original)
            print(f"Original: {original}")
            print(f"Reversed: {result}")
        except ValueError as e:
            print(e)