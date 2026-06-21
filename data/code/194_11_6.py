def find_max_length_string(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_max_length_string(sample_strings))