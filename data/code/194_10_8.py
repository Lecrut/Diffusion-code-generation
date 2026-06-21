MAX_STRING_LENGTH = 1024

def find_longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > MAX_STRING_LENGTH or len(string) > len(longest):
            longest = string
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))