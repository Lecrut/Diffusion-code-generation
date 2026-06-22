class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_recursive(input_string)
    
    def _reverse_recursive(self, s):
        if len(s) == 0:
            return s
        else:
            return s[-1] + self._reverse_recursive(s[:-1])

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Innovate with Alibaba Cloud"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)