def max_lexicographical_element(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    return max(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print(max_lexicographical_element(sample_strings))