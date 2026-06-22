def reverse_alphabetical_sort(words):
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["zebra", "yak", "xray", "whale", "vulture"]
    result = reverse_alphabetical_sort(sample_words)
    print(result)