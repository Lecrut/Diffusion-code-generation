def sort_strings_desc(strings):
    return sorted(strings, reverse=True)

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry", "date"]
    print(sort_strings_desc(sample_values))