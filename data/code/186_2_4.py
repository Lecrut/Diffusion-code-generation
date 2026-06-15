import operator
def case_insensitive_sort(words):
    return sorted(words, key=str.lower)
if __name__ == '__main__':
    word_list = ["Apple", "banana", "Cherry", "date", "apricot"]
    sorted_list = case_insensitive_sort(word_list)
    print(sorted_list)