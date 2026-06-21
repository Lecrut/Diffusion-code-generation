def get_longest_item(string_list):
    if not string_list:
        return ""
    
    longest_string = max(string_list, key=len)
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = get_longest_item(sample_list)
    print(result)