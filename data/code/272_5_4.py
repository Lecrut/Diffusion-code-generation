def reverse_alphabetical_sort(words):
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["grape", "fig", "elderberry", "cherry", "banana"]
    result = reverse_alphabetical_sort(sample_words)
    print(result)