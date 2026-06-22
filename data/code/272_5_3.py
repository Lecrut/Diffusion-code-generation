def reverse_alphabetical_sort(words):
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    print(reverse_alphabetical_sort(sample_words))