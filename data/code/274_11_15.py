def reverse_strings(string_list):
    if not all(isinstance(item, str) for item in string_list):
        raise ValueError("All items in the list must be strings")
    return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reversed_values = reverse_strings(sample_values)
    print(reversed_values)