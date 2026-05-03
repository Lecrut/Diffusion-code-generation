class StringReverser:
    def reverse(self, text):
        return text[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_string1 = "hello"
    reversed_string1 = reverser.reverse(sample_string1)
    print(f"Original: {sample_string1}, Reversed: {reversed_string1}")
    sample_string2 = "world"
    reversed_string2 = reverser.reverse(sample_string2)
    print(f"Original: {sample_string2}, Reversed: {reversed_string2}")
    sample_string3 = "Python"
    reversed_string3 = reverser.reverse(sample_string3)
    print(f"Original: {sample_string3}, Reversed: {reversed_string3}")