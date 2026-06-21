def find_longest_string(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    longest_string = find_longest_string(sample_strings)
    print(longest_string)