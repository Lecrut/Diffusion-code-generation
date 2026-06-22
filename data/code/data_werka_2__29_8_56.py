class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_with_slicing(input_string)
    
    def _reverse_with_slicing(self, s):
        return s[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string1 = "Hello, World!"
    sample_string2 = "Alibaba Cloud"
    sample_string3 = "Qwen, a large language model"
    
    print(reverser.reverse(sample_string1))
    print(reverser.reverse(sample_string2))
    print(reverser.reverse(sample_string3))