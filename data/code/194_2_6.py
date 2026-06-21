def longest_string(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(longest_string(sample_strings))