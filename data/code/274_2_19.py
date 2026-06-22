class StringReverser:
    def reverse_strings(self, string_list):
        return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reverser = StringReverser()
    reversed_values = reverser.reverse_strings(sample_values)
    for value in reversed_values:
        print(value)