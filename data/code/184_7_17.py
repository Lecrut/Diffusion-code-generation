import pandas as pd

def check_word_presence(df_column, word):
    word_set = set(df_column)
    return word in word_set

if __name__ == '__main__':
    data = {'words': ['apple', 'banana', 'cherry']}
    df = pd.DataFrame(data)
    print(check_word_presence(df['words'], 'banana'))