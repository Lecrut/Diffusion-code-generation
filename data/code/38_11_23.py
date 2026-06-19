class StringAnalyzer:
    def __init__(self, text):
        self.text = text.lower()
    
    def check_for_duplicates(self):
        char_count = {}
        for char in self.text:
            if 'a' <= char <= 'z':
                char_count[char] = char_count.get(char, 0) + 1
        duplicates = {char for char, count in char_count.items() if count > 1}
        return sorted(duplicates)

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "programming"
    sample3 = "aabbccddeeffg"
    sample4 = "abcde"

    analyzer1 = StringAnalyzer(sample1)
    print(analyzer1.check_for_duplicates())

    analyzer2 = StringAnalyzer(sample2)
    print(analyzer2.check_for_duplicates())

    analyzer3 = StringAnalyzer(sample3)
    print(analyzer3.check_for_duplicates())

    analyzer4 = StringAnalyzer(sample4)
    print(analyzer4.check_for_duplicates())