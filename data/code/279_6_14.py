def reverse_strings(string_list):
    for s in string_list:
        print(s[::-1])

if __name__ == '__main__':
    sample_values = ["hello", "world", "python", "programming"]
    reverse_strings(sample_values)