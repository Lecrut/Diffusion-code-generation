class StringReverser:
    def reverse(self, text):
        return self._reverse_string(text)

    @staticmethod
    def _reverse_string(s):
        reversed_chars = []
        for char in s:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string_1 = "example"
    reversed_string_1 = reverser.reverse(sample_string_1)
    print(f"Original: {sample_string_1}, Reversed: {reversed_string_1}")
    
    sample_string_2 = "test"
    reversed_string_2 = reverser.reverse(sample_string_2)
    print(f"Original: {sample_string_2}, Reversed: {reversed_string_2}")

    sample_string_3 = "openai"
    reversed_string_3 = reverser.reverse(sample_string_3)
    print(f"Original: {sample_string_3}, Reversed: {reversed_string_3}")