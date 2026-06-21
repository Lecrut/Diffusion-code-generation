import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return bool(word_set.intersection(df[column_name]))

if __name__ == '__main__':
    sample_df = pd.DataFrame({'description': ['python is awesome', 'pandas library', 'data manipulation']})
    search_word = 'awesome'
    result = check_word_presence(sample_df, 'description', search_word)
    print(result)