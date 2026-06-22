class StringReverser:
    def __init__(self, string_list):
        self.string_list = string_list

    def reverse_strings(self):
        return self.string_list[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    reverser = StringReverser(sample_values)
    reversed_values = reverser.reverse_strings()
    print(reversed_values)