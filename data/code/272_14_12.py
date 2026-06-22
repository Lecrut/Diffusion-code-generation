def validate_input(words):
    if not isinstance(words, list):
        raise ValueError("Input must be a list")
    for item in words:
        if not isinstance(item, str):
            raise ValueError("All elements in the list must be strings")

def sort_words(words):
    validate_input(words)
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    print(sort_words(sample_words))