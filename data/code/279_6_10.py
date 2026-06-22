class StringReverser:
    def __init__(self, string_list):
        self.string_list = string_list

    def reverse_strings(self):
        return [s[::-1] for s in self.string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    reverser = StringReverser(sample_values)
    reversed_strings = reverser.reverse_strings()
    print(reversed_strings)