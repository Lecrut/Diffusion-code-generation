MAX_LEN = 0

def find_longest_string(string_list):
    global MAX_LEN
    longest_string = ""
    for s in string_list:
        if len(s) > MAX_LEN:
            longest_string = s
            MAX_LEN = len(s)
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = find_longest_string(sample_list)
    print(result)