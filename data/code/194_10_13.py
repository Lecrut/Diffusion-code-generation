MAX_LENGTH = 0

def find_longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > MAX_LENGTH:
            longest = string
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))