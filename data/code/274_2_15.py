class StringReverser:
    def __init__(self, string_list):
        self.string_list = string_list

    def reverse(self):
        return self.string_list[::-1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reverser = StringReverser(sample_values)
    reversed_values = reverser.reverse()
    for value in reversed_values:
        print(value)