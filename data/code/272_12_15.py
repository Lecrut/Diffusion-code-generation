def validate_input(word_list):
    if not all(isinstance(word, str) for word in word_list):
        raise ValueError("All elements in the list must be strings")

def sort_words(words):
    validate_input(words)
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "zebra", "cat", "dog"]
    sorted_words = sort_words(sample_words)
    print(sorted_words)