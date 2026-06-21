class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_string(input_string)
    
    def _reverse_string(self, s):
        reversed_chars = []
        for char in s:
            reversed_chars.append(char)
        reversed_chars.reverse()
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Qwen, a large language model"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)