def sort_words_by_length(word_list):
    if not isinstance(word_list, list):
        raise ValueError('Input must be a list')
    for item in word_list:
        if not isinstance(item, str):
            raise ValueError('All items in the list must be strings')
    return sorted(word_list, key=len)
if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'kiwi', 'orange', 'grapefruit']
    sorted_list = sort_words_by_length(sample_words)
    print(sorted_list)