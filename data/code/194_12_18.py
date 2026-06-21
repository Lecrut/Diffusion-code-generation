def find_longest_string(string_list):
    if not string_list:
        return None
    longest_string = string_list[0]
    for s in string_list[1:]:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string

if __name__ == '__main__':
    data1 = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result1 = find_longest_string(data1)
    print(f"Data: {data1}")
    print(f"Longest string: {result1}")
    data2 = ["short", "longer", "longestword", "medium"]
    result2 = find_longest_string(data2)
    print(f"Data: {data2}")
    print(f"Longest string: {result2}")