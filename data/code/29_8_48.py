class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self._reverse_recursive(input_string)
    
    def _reverse_recursive(self, s):
        if len(s) == 0:
            return ""
        else:
            return s[-1] + self._reverse_recursive(s[:-1])

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