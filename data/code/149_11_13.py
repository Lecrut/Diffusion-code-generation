class StringReverser:
    def __init__(self, strings):
        self.strings = strings

    def reverse(self):
        self.strings.reverse()

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    reverser = StringReverser(sample_strings)
    print("Original list:", sample_strings)
    reverser.reverse()
    print("Reversed list:", sample_strings)