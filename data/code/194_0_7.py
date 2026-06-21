class StringProcessor:
    @staticmethod
    def find_longest_string(string_list):
        if not string_list:
            return None
        return max(string_list, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    processor = StringProcessor()
    longest_str = processor.find_longest_string(sample_strings)
    print(longest_str)