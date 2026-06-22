def reverse_strings(string_list):
    return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["Hello", "world", "!"]
    reversed_values = reverse_strings(sample_values)
    for value in reversed_values:
        print(value)