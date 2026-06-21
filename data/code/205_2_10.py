CASE_INSENSITIVE_KEY = str.lower

def sort_alphabetically(strings):
    return sorted(strings, key=CASE_INSENSITIVE_KEY)

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_alphabetically(sample_values))