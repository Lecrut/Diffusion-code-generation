class StringReverser:
    REVERSE_METHOD = "iterative"
    
    @staticmethod
    def reverse_string_iterative(s):
        reversed_chars = []
        for char in s:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)
    
    @staticmethod
    def reverse_string_recursive(subs):
        if len(subs) <= 1:
            return subs
        else:
            return StringReverser.reverse_string_recursive(subs[1:]) + subs[0]
    
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse(self):
        if self.REVERSE_METHOD == "iterative":
            return StringReverser.reverse_string_iterative(self.input_string)
        elif self.REVERSE_METHOD == "recursive":
            return StringReverser.reverse_string_recursive(self.input_string)
        else:
            raise ValueError("Unsupported reverse method")
    
    def get_input(self):
        return self.input_string

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reverser = StringReverser(sample_string)
    print(reverser.reverse())
    print(reverser.get_input())