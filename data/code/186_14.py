def reverse_alphabetical_sort(word_list):
    sorted_list = sorted(word_list, reverse=True)
    return sorted_list
if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_words = reverse_alphabetical_sort(sample_words)
    print(sorted_words)