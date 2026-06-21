class StringFinder:
    @staticmethod
    def find_longest(strings):
        if not strings:
            return ""
        longest = max(strings, key=len)
        return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringFinder.find_longest(sample_list)
    print(result)