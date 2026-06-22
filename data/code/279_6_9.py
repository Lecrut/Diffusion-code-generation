def reverse_strings(string_list):
    if not all(isinstance(s, str) for s in string_list):
        raise ValueError("All elements in the list must be strings")
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    reversed_strings = reverse_strings(sample_values)
    print(reversed_strings)