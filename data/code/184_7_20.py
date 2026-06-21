import pandas as pd

def convert_to_set(column):
    return set(item.split() for item in column)

def is_word_present(df, column_name, word):
    words_to_check = {word}
    word_set = convert_to_set(df[column_name])
    return words_to_check.issubset(word_set)

if __name__ == '__main__':
    sample_df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux']})
    print(is_word_present(sample_df, 'text', 'world'))