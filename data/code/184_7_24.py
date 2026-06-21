import pandas as pd

class WordPresenceChecker:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        self.word_set = set()

    def preprocess_column(self):
        self.df[self.column_name] = self.df[self.column_name].astype(str)

    def build_word_set(self, word):
        self.word_set.update(word.split())

    def check_presence(self, word):
        if not self.word_set:
            raise ValueError("Word set is empty. Call build_word_set first.")
        return word in self.word_set

if __name__ == '__main__':
    sample_df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux']})
    checker = WordPresenceChecker(sample_df, 'text')
    checker.preprocess_column()
    checker.build_word_set('world')
    print(checker.check_presence('world'))