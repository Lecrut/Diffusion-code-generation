class WordMatcher:
    def __init__(self, word_dict):
        self.word_dict = word_dict
    def get_sorted_words(self):
        return sorted(self.word_dict.keys())
if __name__ == '__main__':
    sample_data = {
        "apple": 5,
        "banana": 10,
        "cherry": 3,
        "date": 7
    }
    matcher = WordMatcher(sample_data)
    sorted_list = matcher.get_sorted_words()
    print(sorted_list)