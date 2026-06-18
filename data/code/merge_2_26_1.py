import csv
from typing import Dict
def load_dictionary(filepath: str) -> Dict[str, list]:
    dictionary = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)                              
        for word in reader:
            definition_list = []
            for defn in word[1:]:
                definition_list.append(defn.strip())
            dictionary[word[0].strip()] = definition_list
    return dictionary
if __name__ == '__main__':
    data_dict = load_dictionary('sample_data.csv')
    sample_word = 'apple'
    if sample_word in data_dict:
        print(f"Definitions for {sample_word}:")
        for i, defn in enumerate(data_dict[sample_word], 1):
            print(f"{i}. {defn}")
    else:
        print("Word not found.")