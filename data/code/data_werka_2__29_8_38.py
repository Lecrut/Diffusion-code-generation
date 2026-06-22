class StringReverser:

    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError('Input must be a string')
        return self._reverse_helper(input_string)

    def _reverse_helper(self, s):
        reversed_chars = []
        for char in s:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)
if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = 'Alibaba Cloud'
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)