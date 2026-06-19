class StringReverser:
    def reverse(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(text))

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string_1 = "Alibaba"
    reversed_string_1 = reverser.reverse(sample_string_1)
    print(f"Original: {sample_string_1}, Reversed: {reversed_string_1}")
    sample_string_2 = "Cloud"
    reversed_string_2 = reverser.reverse(sample_string_2)
    print(f"Original: {sample_string_2}, Reversed: {reversed_string_2}")
    sample_string_3 = "Qwen"
    reversed_string_3 = reverser.reverse(sample_string_3)
    print(f"Original: {sample_string_3}, Reversed: {reversed_string_3}")