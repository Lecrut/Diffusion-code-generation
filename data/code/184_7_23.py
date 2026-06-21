import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return word in word_set

if __name__ == '__main__':
    data = {'text': ['hello world', 'foo bar', 'baz qux']}
    df = pd.DataFrame(data)
    print(check_word_presence(df, 'text', 'world'))