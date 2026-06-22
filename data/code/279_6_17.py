def print_reversed_strings(string_list):
    for s in string_list:
        print(s[::-1])

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print_reversed_strings(sample_values)