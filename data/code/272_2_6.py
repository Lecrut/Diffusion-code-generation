def validate_input(word_list):
    if not isinstance(word_list, list) or not all(isinstance(item, str) for item in word_list):
        raise ValueError("Input must be a list of strings")

def sort_words(words):
    validate_input(words)
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    print(sort_words(sample_words))