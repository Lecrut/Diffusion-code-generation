def sort_strings_desc(strings):
    return sorted(strings, reverse=True)

if __name__ == '__main__':
    sample_values = ["dog", "cat", "banana", "zebra", "apple"]
    result = sort_strings_desc(sample_values)
    print(result)