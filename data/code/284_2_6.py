def reverse_strings_in_list(strings):
    return [s[::-1] for s in strings]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    reversed_values = reverse_strings_in_list(sample_values)
    print(reversed_values)