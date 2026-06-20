def sort_strings_by_length_and_alphabet(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    return sorted(strings, key=lambda x: (-len(x), x))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date", "elderberry"]
    sorted_list = sort_strings_by_length_and_alphabet(sample_values)
    print(sorted_list)