def reverse_alphabetical_sort(word_list):
    return sorted(word_list, reverse=True)

if __name__ == '__main__':
    sample_list = ["banana", "apple", "date", "cherry", "elderberry"]
    result = reverse_alphabetical_sort(sample_list)
    print(result)