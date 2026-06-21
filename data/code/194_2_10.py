class StringFinder:
    @staticmethod
    def find_longest(strings):
        if not strings:
            return ""
        longest = ""
        for string in strings:
            if len(string) > len(longest):
                longest = string
        return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringFinder.find_longest(sample_list)
    print(result)