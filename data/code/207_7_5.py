def find_max_string(list_of_strings):
    if not list_of_strings:
        return None
    max_string = list_of_strings[0]
    for s in list_of_strings[1:]:
        if s > max_string:
            max_string = s
    return max_string
if __name__ == '__main__':
    list1 = ["apple", "zebra", "banana", "cat"]
    result1 = find_max_string(list1)
    print(f"List: {list1}, Max: {result1}")
    list2 = ["zoo", "ant", "bear", "lion"]
    result2 = find_max_string(list2)
    print(f"List: {list2}, Max: {result2}")
    list3 = ["a", "b", "c", "aa", "bb"]
    result3 = find_max_string(list3)
    print(f"List: {list3}, Max: {result3}")
    list4 = []
    result4 = find_max_string(list4)
    print(f"List: {list4}, Max: {result4}")