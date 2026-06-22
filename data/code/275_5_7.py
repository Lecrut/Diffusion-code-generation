MAX_LEN = 0

def find_longest_string(strings):
    global MAX_LEN
    longest = ""
    for s in strings:
        if len(s) > MAX_LEN:
            longest = s
            MAX_LEN = len(s)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))