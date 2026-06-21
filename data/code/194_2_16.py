MAX_LEN = -1

def get_longest_item(string_list):
    if not string_list:
        return ""
    
    longest_string = ""
    max_length = MAX_LEN
    
    for item in string_list:
        current_length = len(item)
        if current_length > max_length:
            max_length = current_length
            longest_string = item
            
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = get_longest_item(sample_list)
    print(result)