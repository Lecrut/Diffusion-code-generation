class StringReverser:
    def reverse(self, s):
        return s[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    test_string_1 = "hello"
    reversed_1 = reverser.reverse(test_string_1)
    print(f"Original: {test_string_1}, Reversed: {reversed_1}")
    test_string_2 = "world"
    reversed_2 = reverser.reverse(test_string_2)
    print(f"Original: {test_string_2}, Reversed: {reversed_2}")
    test_string_3 = "Python"
    reversed_3 = reverser.reverse(test_string_3)
    print(f"Original: {test_string_3}, Reversed: {reversed_3}")