class StringProcessor:
    def __init__(self, string_list):
        self.string_list = string_list

    def find_longest_string(self):
        if not self.string_list:
            return ""
        longest_string = self.string_list[0]
        for s in self.string_list:
            if len(s) > len(longest_string):
                longest_string = s
        return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    processor = StringProcessor(sample_strings)
    result = processor.find_longest_string()
    print(result)