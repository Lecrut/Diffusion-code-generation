SORT_KEY = lambda s: s.lower()

def sort_strings_case_insensitive(strings):
    return sorted(strings, key=SORT_KEY)

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_strings_case_insensitive(sample_values))