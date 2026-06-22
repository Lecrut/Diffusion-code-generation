def reverse_strings(string_list):
    return [string[::-1] for string in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    reversed_values = reverse_strings(sample_values)
    for value in reversed_values:
        print(value)