MAX_LENGTH = -1

def find_longest_string(list_of_lists):
    longest_string = ""
    for inner_list in list_of_lists:
        for item in inner_list:
            if len(item) > MAX_LENGTH:
                MAX_LENGTH = len(item)
                longest_string = item
    return longest_string

if __name__ == '__main__':
    sample_data = [
        ["apple", "banana", "kiwi"],
        ["grapefruit", "orange", "melon"],
        ["strawberry", "pineapple", "avocado"]
    ]
    result = find_longest_string(sample_data)
    print(result)