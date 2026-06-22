def print_reversed_strings(string_list):
    for item in reversed(string_list):
        print(item)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    print_reversed_strings(sample_values)