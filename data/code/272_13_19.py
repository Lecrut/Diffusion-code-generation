def validate_input(words):
    if not all(isinstance(item, str) for item in words):
        raise ValueError("All items in the list must be strings")

def sort_words(words):
    validate_input(words)
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    print(sort_words(sample_words))