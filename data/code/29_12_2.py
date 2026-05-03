class StringReverser:
    def reverse(self, s):
        return s[::-1]
if __name__ == '__main__':
    reverser = StringReverser()
    sample_string1 = "hello"
    sample_string2 = "world"
    sample_string3 = "Python"
    reversed1 = reverser.reverse(sample_string1)
    reversed2 = reverser.reverse(sample_string2)
    reversed3 = reverser.reverse(sample_string3)
    print(reversed1)
    print(reversed2)
    print(reversed3)