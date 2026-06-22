def reverse_alphabetical_sort(word_list):
    if not all(isinstance(item, str) for item in word_list):
        raise ValueError("All items in the list must be strings.")
    return sorted(word_list, reverse=True)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    print(reverse_alphabetical_sort(sample_words))