class StringAnalyzer:
    def __init__(self, text):
        self.text = text

    def check_for_duplicates(self):
        letter_counts = {}
        for char in self.text:
            if 'a' <= char <= 'z':
                letter_counts[char] = letter_counts.get(char, 0) + 1
            elif 'A' <= char <= 'Z':
                letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1
        repeated_letters = set()
        for letter, count in letter_counts.items():
            if count > 1:
                repeated_letters.add(letter)
        return repeated_letters

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