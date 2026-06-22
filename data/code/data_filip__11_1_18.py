import collections

def find_duplicate_characters(text):
    if not text:
        return []
    counts = collections.Counter(text)
    duplicates = sorted({char for char, count in counts.items() if count > 1})
    return duplicates

class TextAnalyzer:
    def __init__(self, content):
        self.content = content

    def get_duplicates(self):
        return find_duplicate_characters(self.content)

if __name__ == '__main__':
    test_string = "hello world"
    analyzer = TextAnalyzer(test_string)
    print(analyzer.get_duplicates())
    another_string = "Mississippi"
    analyzer.content = another_string
    print(analyzer.get_duplicates())