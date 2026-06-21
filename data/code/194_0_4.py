def find_longest_string(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))