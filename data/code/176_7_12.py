class DistinctWordParser:
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def parse(self):
        words = self.paragraph.split()
        distinct_words = sorted(set(words))
        return distinct_words

if __name__ == '__main__':
    parser_instance = DistinctWordParser("This is a sample paragraph with some repeated words. This is just for demonstration.")
    result = parser_instance.parse()
    print(result)