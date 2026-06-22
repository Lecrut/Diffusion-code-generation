def reverse_strings(string_list):
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise ValueError("Input must be a list of strings")
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print(reverse_strings(sample_values))