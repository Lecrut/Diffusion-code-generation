def sort_by_length_descending(string_list):
    return sorted(string_list, key=len, reverse=True)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_by_length_descending(sample_list)
    print(sorted_list)