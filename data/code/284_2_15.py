class StringReverser:
    @staticmethod
    def reverse_strings(string_list):
        return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "python"]
    reversed_sample = StringReverser.reverse_strings(sample_values)
    print(reversed_sample)