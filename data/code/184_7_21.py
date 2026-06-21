import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return word in word_set

if __name__ == '__main__':
    data = {'text': ['apple banana', 'orange apple', 'banana orange']}
    df = pd.DataFrame(data)
    result = check_word_presence(df, 'text', 'apple')
    print(result)