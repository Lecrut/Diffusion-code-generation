def print_reverse(strings):
    for string in reversed(strings):
        print(string)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "this", "is", "a", "test"]
    print_reverse(sample_strings)