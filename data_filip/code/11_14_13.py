import collections

def count_character_duplicates(text):
    frequency_map = collections.Counter(text)
    duplicates = {char: count for char, count in frequency_map.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "programming"
    result = count_character_duplicates(sample_text)
    print(result)