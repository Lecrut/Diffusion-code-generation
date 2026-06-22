def reverse_strings(string_list):
    return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["Hello", "world", "this", "is", "a", "test"]
    reversed_list = reverse_strings(sample_values)
    print(reversed_list)