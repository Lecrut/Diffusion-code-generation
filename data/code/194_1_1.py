import time
def find_longest_list_item(list_of_strings):
    if not list_of_strings:
        return ""
    longest_string = ""
    for s in list_of_strings:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_list)
    print(result)