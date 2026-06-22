def reverse_alphabetical_sort(word_list):
    return sorted(word_list, reverse=True)

if __name__ == '__main__':
    sample_words = ["orange", "grape", "apple", "kiwi"]
    result = reverse_alphabetical_sort(sample_words)
    print(result)