import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return word in word_set

if __name__ == '__main__':
    sample_df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux']})
    print(check_word_presence(sample_df, 'text', 'world'))