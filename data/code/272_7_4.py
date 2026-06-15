def alphabetical_sort(string_iterable):
    return sorted(list(string_iterable))
if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = alphabetical_sort(sample_data)
    print(sorted_result)