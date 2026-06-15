def find_max_string(list_of_strings):
    if not list_of_strings:
        return None
    max_string = list_of_strings[0]
    for s in list_of_strings:
        if s > max_string:
            max_string = s
    return max_string
if __name__ == '__main__':
    sample1 = ["apple", "zebra", "banana", "cat"]
    result1 = find_max_string(sample1)
    print(f"Sample 1: {sample1}")
    print(f"Maximum string in Sample 1: {result1}")
    sample2 = ["zoo", "ant", "bear", "cat"]
    result2 = find_max_string(sample2)
    print(f"Sample 2: {sample2}")
    print(f"Maximum string in Sample 2: {result2}")
    sample3 = ["a", "b", "c", "aa"]
    result3 = find_max_string(sample3)
    print(f"Sample 3: {sample3}")
    print(f"Maximum string in Sample 3: {result3}")
    sample4 = []
    result4 = find_max_string(sample4)
    print(f"Sample 4: {sample4}")
    print(f"Maximum string in Sample 4: {result4}")