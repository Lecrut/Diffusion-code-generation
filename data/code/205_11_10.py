def sort_items(data):
    return sorted(data, key=str.lower)

if __name__ == '__main__':
    unsorted_strings = ["apple", "Banana", "cherry", "date"]
    sorted_strings = sort_items(unsorted_strings)
    print(sorted_strings)