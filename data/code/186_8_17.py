def validate_input(word_list):
    if not all(isinstance(item, str) for item in word_list):
        raise ValueError("All elements in the list must be strings.")
    return True

def sort_words_by_length(word_list):
    validate_input(word_list)
    return sorted(word_list, key=len)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_words_by_length(sample_words)
    print(sorted_list)