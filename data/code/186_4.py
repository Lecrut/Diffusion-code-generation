def process_words(word_list):
    unique_words = set(word_list)
    sorted_words = sorted(list(unique_words))
    return sorted_words
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "apple", "date", "banana"]
    result = process_words(sample_list)
    print(result)