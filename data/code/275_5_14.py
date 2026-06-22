class StringProcessor:
    @staticmethod
    def find_longest_string(strings):
        longest = ""
        for s in strings:
            if len(s) > len(longest):
                longest = s
        return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    processor = StringProcessor()
    print(processor.find_longest_string(sample_strings))