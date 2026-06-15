def find_lexicographically_maximum(string_list):
    if not string_list:
        return None
    max_string = string_list[0]
    for s in string_list:
        if s > max_string:
            max_string = s
    return max_string
if __name__ == '__main__':
    list1 = ["apple", "zebra", "banana", "cat"]
    result1 = find_lexicographically_maximum(list1)
    print(f"List: {list1}")
    print(f"Maximum lexicographical string: {result1}")
    list2 = ["hello", "world", "python", "java"]
    result2 = find_lexicographically_maximum(list2)
    print(f"List: {list2}")
    print(f"Maximum lexicographical string: {result2}")
    list3 = ["a", "b", "c", "aa", "z"]
    result3 = find_lexicographically_maximum(list3)
    print(f"List: {list3}")
    print(f"Maximum lexicographical string: {result3}")
    list4 = []
    result4 = find_lexicographically_maximum(list4)
    print(f"List: {list4}")
    print(f"Maximum lexicographical string: {result4}")