MAX_STRING_LENGTH = 0

def find_longest_string(strings):
    global MAX_STRING_LENGTH
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
            MAX_STRING_LENGTH = len(longest)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))