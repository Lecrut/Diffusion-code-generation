def reverse_strings(string_list):
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample = ["hello", "world", "!"]
    print(reverse_strings(sample))