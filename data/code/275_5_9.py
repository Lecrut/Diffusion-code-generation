class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def find_longest_string(self):
        longest = ""
        for string in self.strings:
            if len(string) > len(longest):
                longest = string
        return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    processor = StringProcessor(sample_strings)
    print(processor.find_longest_string())