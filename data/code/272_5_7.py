def reverse_alphabetical_sort(word_list):
    return sorted(word_list, reverse=True)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    print(reverse_alphabetical_sort(sample_words))