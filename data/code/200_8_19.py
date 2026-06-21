from collections import Counter

def count_word_occurrences(word_list):
    if not isinstance(word_list, list) or not all((isinstance(item, str) for item in word_list)):
        raise ValueError('Input must be a list of strings')
    return Counter(word_list)
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    result = count_word_occurrences(sample_list)
    print(result)