def sort_strings(strings):
    return sorted(strings, key=lambda s: (s[0].isupper(), s))
if __name__ == '__main__':
    sample_list = ["apple", "Banana", "cherry", "Date", "elderberry"]
    print(sort_strings(sample_list))