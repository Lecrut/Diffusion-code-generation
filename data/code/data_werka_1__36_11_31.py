class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

if __name__ == '__main__':
    reverser_short = StringReverser("hello")
    print(f"Original: {reverser_short.input_string}, Reversed: {reverser_short.reverse()}")
    
    long_string = "this is a test string for optimization" * 1000
    reverser_long = StringReverser(long_string)
    print(f"Original length: {len(reverser_long.input_string)}")
    print(f"Reversed (first 50 chars): {reverser_long.reverse()[:50]}...")