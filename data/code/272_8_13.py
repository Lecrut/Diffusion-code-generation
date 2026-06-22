def validate_input(word_list):
    if not isinstance(word_list, list) or not all(isinstance(word, str) for word in word_list):
        raise ValueError("Input must be a list of strings")

def sort_words(word_list):
    validate_input(word_list)
    sorted_word_list = sorted(word_list)
    return sorted_word_list

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    print("Original sequence:", sample_words)
    sorted_sample_words = sort_words(sample_words)
    print("Sorted list of words:", sorted_sample_words)