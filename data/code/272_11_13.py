def validate_word_list(word_list):
    if not all(isinstance(item, str) for item in word_list):
        raise ValueError("All elements in the list must be strings")

def sort_words(word_list):
    validate_word_list(word_list)
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = sort_words(sample_words)
    print(sorted_result)