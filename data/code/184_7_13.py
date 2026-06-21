import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(df[column_name])
    return word in word_set

if __name__ == '__main__':
    data = {'words': ['apple', 'banana', 'cherry']}
    df = pd.DataFrame(data)
    print(check_word_presence(df, 'words', 'banana'))