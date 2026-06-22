def reverse_strings(string_list):
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "!"]
    reversed_strings = reverse_strings(sample_strings)
    print(reversed_strings)