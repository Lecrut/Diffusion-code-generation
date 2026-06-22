class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_with_map(input_string)
    
    def _reverse_with_map(self, s):
        char_map = {i: char for i, char in enumerate(s)}
        reversed_chars = [char_map[i] for i in range(len(s) - 1, -1, -1)]
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Innovate with Qwen"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)