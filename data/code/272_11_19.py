def validate_input(word_list):
    if not isinstance(word_list, list):
        raise ValueError("Input must be a list")
    for item in word_list:
        if not isinstance(item, str):
            raise ValueError("All items in the list must be strings")

def sort_words(word_list):
    validate_input(word_list)
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = sort_words(sample_words)
    print(sorted_result)