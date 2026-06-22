def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    words = ["orange", "grape", "apple", "banana", "pineapple"]
    sorted_words = sort_words(words)
    print(*sorted_words)