LENGTH_KEY = 'length'

def sort_words_by_length(word_list):
    return sorted(word_list, key=lambda word: len(word))

if __name__ == '__main__':
    sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_words_by_length(sample_words)
    print(sorted_list)