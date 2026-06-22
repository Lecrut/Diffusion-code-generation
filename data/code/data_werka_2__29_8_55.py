class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_with_slices(input_string)
    
    def _reverse_with_slices(self, s):
        return s[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "OpenAI GPT-4"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)