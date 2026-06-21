def sort_alphabetically(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_values = ["apple", "Cherry", "banana", "Date"]
    sorted_list = sort_alphabetically(sample_values)
    print(sorted_list)