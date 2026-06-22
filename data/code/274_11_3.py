def reverse_strings(string_list):
    return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    reversed_values = reverse_strings(sample_values)
    print(reversed_values)