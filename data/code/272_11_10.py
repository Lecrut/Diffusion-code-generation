def validate_input(word_list):
    if not isinstance(word_list, list) or not all(isinstance(word, str) for word in word_list):
        raise ValueError("Input must be a list of strings")

def sort_words(word_list):
    validate_input(word_list)
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = sort_words(sample_words)
    print(sorted_result)