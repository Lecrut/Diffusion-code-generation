MAX_LENGTH = 0

def find_longest_string(strings):
    global MAX_LENGTH
    longest_string = ""
    for string in strings:
        if len(string) > MAX_LENGTH:
            MAX_LENGTH = len(string)
            longest_string = string
    return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    result = find_longest_string(sample_strings)
    print(result)