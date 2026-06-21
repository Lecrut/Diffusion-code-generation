class StringProcessor:
    def __init__(self, string_list):
        self.string_list = string_list

    def find_longest_string(self):
        if not self.string_list:
            return ""
        longest_string = max(self.string_list, key=len)
        return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    processor = StringProcessor(sample_list)
    result = processor.find_longest_string()
    print(result)