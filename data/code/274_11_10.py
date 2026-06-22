class StringReverser:
    @staticmethod
    def reverse_string_list(string_list):
        return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reversed_values = StringReverser.reverse_string_list(sample_values)
    for item in reversed_values:
        print(item)