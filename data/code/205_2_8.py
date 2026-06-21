def sort_alphabetically(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_alphabetically(sample_values))