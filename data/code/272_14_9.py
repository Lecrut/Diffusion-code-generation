def validate_input(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")

def sort_words(words):
    validate_input(words)
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    print(sort_words(sample_words))