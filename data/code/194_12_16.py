MAX_STRING_LENGTH = 1000

def find_longest_string(string_list):
    if not string_list:
        return None
    longest_string = ""
    for s in string_list:
        if len(s) > len(longest_string) and len(s) <= MAX_STRING_LENGTH:
            longest_string = s
    return longest_string

if __name__ == '__main__':
    data1 = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result1 = find_longest_string(data1)
    print(f"Data: {data1}")
    print(f"Longest string: {result1}")
    
    data2 = ["short", "longer", "longest", "test"]
    result2 = find_longest_string(data2)
    print(f"Data: {data2}")
    print(f"Longest string: {result2}")