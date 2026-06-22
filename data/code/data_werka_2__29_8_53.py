class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_with_two_pointers(input_string)
    
    @staticmethod
    def _reverse_with_two_pointers(s):
        char_list = list(s)
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string1 = "Hello, World!"
    sample_string2 = "Alibaba Cloud"
    sample_string3 = "Qwen, a large language model"

    reversed_string1 = reverser.reverse(sample_string1)
    reversed_string2 = reverser.reverse(sample_string2)
    reversed_string3 = reverser.reverse(sample_string3)

    print(reversed_string1)
    print(reversed_string2)
    print(reversed_string3)