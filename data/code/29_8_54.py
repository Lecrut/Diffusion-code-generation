class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_recursive(input_string)
    
    def _reverse_recursive(self, s, index=None):
        if index is None:
            index = len(s) - 1
        if index < 0:
            return ""
        return s[index] + self._reverse_recursive(s, index - 1)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Innovate with Alibaba Cloud"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)