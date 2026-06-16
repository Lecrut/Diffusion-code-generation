import math
def find_longest_strings(string_list):
    if not string_list:
        return []
    max_length = 0
    for s in string_list:
        if len(s) > max_length:
            max_length = len(s)
    longest_strings = []
    for s in string_list:
        if len(s) == max_length:
            longest_strings.append(s)
    return longest_strings
if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    result = find_longest_strings(sample_strings)
    print(result)