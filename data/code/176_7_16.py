class WordParser:
    def __init__(self, text):
        self.text = text

    def parse_and_sort(self):
        words = self.text.split()
        distinct_words = sorted(set(words))
        return distinct_words

if __name__ == '__main__':
    parser_instance = WordParser("This is a sample paragraph with some repeated words. This is just for demonstration.")
    result = parser_instance.parse_and_sort()
    print(result)