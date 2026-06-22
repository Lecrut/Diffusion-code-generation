def reverse_alphabetical_sort(words):
    if not isinstance(words, list) or not all((isinstance(word, str) for word in words)):
        raise ValueError('Input must be a list of strings')
    sorted_words = sorted(words, reverse=True)
    return sorted_words
if __name__ == '__main__':
    sample_words = ['banana', 'apple', 'cherry', 'date']
    print(reverse_alphabetical_sort(sample_words))