import math
def find_longest_strings(list_of_strings):
    if not list_of_strings:
        return []
    max_length = 0
    for s in list_of_strings:
        if len(s) > max_length:
            max_length = len(s)
    longest_strings = []
    for s in list_of_strings:
        if len(s) == max_length:
            longest_strings.append(s)
    return longest_strings
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    result = find_longest_strings(sample_list)
    print(result)