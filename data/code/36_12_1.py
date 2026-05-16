class StringReverser:
    def reverse(self, text):
        return text[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_string_1 = "hello"
    reversed_string_1 = reverser.reverse(sample_string_1)
    print(f"Original: {sample_string_1}, Reversed: {reversed_string_1}")
    sample_string_2 = "world"
    reversed_string_2 = reverser.reverse(sample_string_2)
    print(f"Original: {sample_string_2}, Reversed: {reversed_string_2}")
    sample_string_3 = "Python"
    reversed_string_3 = reverser.reverse(sample_string_3)
    print(f"Original: {sample_string_3}, Reversed: {reversed_string_3}")