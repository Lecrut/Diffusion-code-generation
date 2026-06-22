def validate_input(word_list):
    if not isinstance(word_list, list) or not all(isinstance(word, str) for word in word_list):
        raise ValueError("Input must be a list of strings")

def reverse_alphabetical_sort(words):
    validate_input(words)
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    print(reverse_alphabetical_sort(sample_words))