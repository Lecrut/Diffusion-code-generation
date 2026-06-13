def sort_dictionary_values(data):
    words = list(data.values())
    words.sort()
    return words
if __name__ == '__main__':
    sample_data = {
        "apple": "banana",
        "cat": "dog",
        "zebra": "ant",
        "bear": "lion"
    }
    sorted_words = sort_dictionary_values(sample_data)
    print(sorted_words)