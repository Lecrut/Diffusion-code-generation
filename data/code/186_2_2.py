import operator
def case_insensitive_sort(words):
    return sorted(words, key=str.lower)
if __name__ == '__main__':
    sample_list = ["Apple", "banana", "Cherry", "date", "apricot"]
    sorted_list = case_insensitive_sort(sample_list)
    print(sorted_list)