import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return any(w in word_set for w in df[column_name])

if __name__ == '__main__':
    sample_df = pd.DataFrame({'description': ['Python is great', 'Pandas library', 'Data manipulation tools']})
    word_to_check = 'great'
    result = check_word_presence(sample_df, 'description', word_to_check)
    print(result)