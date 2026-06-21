import pandas as pd

def preprocess_column(df, column_name):
    df[column_name] = df[column_name].astype(str)
    return df

def convert_to_set(words):
    return set(words.split())

def check_word_presence(df, column_name, word):
    preprocessed_df = preprocess_column(df, column_name)
    word_set = convert_to_set(word)
    return any(w in word_set for w in preprocessed_df[column_name])

if __name__ == '__main__':
    sample_df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux']})
    word_to_check = 'world'
    result = check_word_presence(sample_df, 'text', word_to_check)
    print(result)