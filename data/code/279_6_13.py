def reverse_and_print(strings):
    for s in strings:
        print(s[::-1])

if __name__ == '__main__':
    sample_strings = ["hello", "world", "!"]
    reverse_and_print(sample_strings)