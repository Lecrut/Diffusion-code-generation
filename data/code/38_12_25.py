class StringAnalyzer:
    def __init__(self):
        self.char_count = {}

    def check_for_duplicates(self, text):
        for char in text:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1
        return any(count > 1 for count in self.char_count.values())

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = "hello world"
    sample_string2 = "programming"
    sample_string3 = "abcdefg"
    sample_string4 = "aabbccddeeff"
    print(f"'{sample_string1}': {analyzer.check_for_duplicates(sample_string1)}")
    print(f"'{sample_string2}': {analyzer.check_for_duplicates(sample_string2)}")
    print(f"'{sample_string3}': {analyzer.check_for_duplicates(sample_string3)}")
    print(f"'{sample_string4}': {analyzer.check_for_duplicates(sample_string4)}")