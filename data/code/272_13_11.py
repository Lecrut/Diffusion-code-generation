def validate_input(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All items in the list must be strings")

def sort_words(words):
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    try:
        validate_input(sample_words)
        sorted_words = sort_words(sample_words)
        print("Alphabetically sorted list:")
        for word in sorted_words:
            print(word)
    except ValueError as e:
        print(e)