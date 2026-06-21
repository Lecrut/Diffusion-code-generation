class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_iterative(input_string)
    
    def _reverse_iterative(self, s):
        length = len(s)
        reversed_chars = [''] * length
        for i in range(length):
            reversed_chars[length - 1 - i] = s[i]
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Efficient and scalable"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)