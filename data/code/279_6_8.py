def print_strings_reversed(strings):
    for s in strings:
        print(s[::-1])

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print_strings_reversed(sample_values)