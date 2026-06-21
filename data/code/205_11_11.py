def sort_alphabetically(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    unsorted_strings = ["banana", "Apple", "cherry", "date"]
    sorted_strings = sort_alphabetically(unsorted_strings)
    print(sorted_strings)