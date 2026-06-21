import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(df[column_name])
    return word in word_set
if __name__ == '__main__':
    sample_df = pd.DataFrame({'words': ['apple', 'banana', 'cherry', 'date']})
    print(check_word_presence(sample_df, 'words', 'banana'))
    print(check_word_presence(sample_df, 'words', 'grape'))