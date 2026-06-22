class StringReverser:
    REVERSE_METHOD = 'slice'
    
    @staticmethod
    def reverse_slice(s):
        return s[::-1]
    
    @staticmethod
    def reverse_join(s):
        return ''.join(reversed(s))
    
    def __init__(self, text):
        self.text = text
    
    def reverse(self):
        if self.REVERSE_METHOD == 'slice':
            return self.reverse_slice(self.text)
        elif self.REVERSE_METHOD == 'join':
            return self.reverse_join(self.text)
        else:
            raise ValueError("Invalid reverse method specified")

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reverser = StringReverser(sample_string)
    reversed_string = reverser.reverse()
    print(reversed_string)