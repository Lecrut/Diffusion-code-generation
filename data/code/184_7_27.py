import pandas as pd

def check_word_presence(df, column_name, word):
    df[column_name] = df[column_name].astype(str)
    word_set = set(word.split())
    return bool(word_set.intersection(df[column_name]))

if __name__ == '__main__':
    data = {'description': ['Python is great', 'Learning pandas is fun', 'Data science with Python']}
    df = pd.DataFrame(data)
    word_to_check = 'Python'
    result = check_word_presence(df, 'description', word_to_check)
    print(result)