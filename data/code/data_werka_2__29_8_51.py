class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_with_two_pointers(input_string)
    
    def _reverse_with_two_pointers(self, s):
        char_list = list(s)
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "OpenAI GPT-4"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)