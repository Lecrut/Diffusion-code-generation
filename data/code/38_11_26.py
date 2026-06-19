class StringAnalyzer:
    def __init__(self, text):
        self.text = text.lower()
    
    def check_for_duplicates(self):
        char_count = {}
        for char in self.text:
            if 'a' <= char <= 'z':
                char_count[char] = char_count.get(char, 0) + 1
        duplicates = {char for char, count in char_count.items() if count > 1}
        return duplicates

if __name__ == '__main__':
    sample_text_1 = "Hello World"
    sample_text_2 = "Python Programming"
    sample_text_3 = "Mississippi"
    
    analyzer_1 = StringAnalyzer(sample_text_1)
    print(analyzer_1.check_for_duplicates())
    
    analyzer_2 = StringAnalyzer(sample_text_2)
    print(analyzer_2.check_for_duplicates())
    
    analyzer_3 = StringAnalyzer(sample_text_3)
    print(analyzer_3.check_for_duplicates())