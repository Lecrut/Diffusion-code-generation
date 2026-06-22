def find_min_lexicographical(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    return min(strings)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(find_min_lexicographical(sample_values))