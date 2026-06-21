MAX_LENGTH = 0

def find_longest_list_item(string_list):
    global MAX_LENGTH
    if not string_list:
        return ""
    longest_string = ""
    for s in string_list:
        if len(s) > len(longest_string):
            longest_string = s
    MAX_LENGTH = max(MAX_LENGTH, len(longest_string))
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_list)
    print(result)
    print("Maximum length found:", MAX_LENGTH)