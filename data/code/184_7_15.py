import pandas as pd

def convert_column_to_set(df, column_name):
    df[column_name] = df[column_name].astype(str)
    return set(df[column_name].str.split().sum())

def check_word_presence(df, column_name, word):
    word_set = convert_column_to_set(df, column_name)
    return word in word_set

if __name__ == '__main__':
    sample_df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux']})
    print(check_word_presence(sample_df, 'text', 'world'))