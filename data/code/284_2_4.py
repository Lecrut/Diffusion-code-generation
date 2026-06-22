class StringReverser:
    def reverse_strings(self, string_list):
        return [s[::-1] for s in string_list]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_values = ["hello", "world", "!"]
    reversed_sample = reverser.reverse_strings(sample_values)
    print(reversed_sample)