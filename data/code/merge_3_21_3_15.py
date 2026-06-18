def sort_strings(strings):
    """Sorts a list of strings alphabetically (lexicographically)."""
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    result = sort_strings(sample_data)
    print(result)