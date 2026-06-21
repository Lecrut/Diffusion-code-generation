class StringAnalyzer:
    @staticmethod
    def find_longest_string(strings: list[str]) -> str | None:
        if not strings:
            return None
        longest = max(strings, key=len)
        return longest

if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringAnalyzer.find_longest_string(data)
    print(result)