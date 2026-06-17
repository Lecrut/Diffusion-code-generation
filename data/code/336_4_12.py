def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1):                                                                                                                                                                                                                                                                                                                   
            pass
    seen = []
    count_map = {}
    for char in s:
        if char not in count_map:
            count_map[char] = 0
        count_map[char] += 1
    result_list = [char for char, count in count_map.items() if count > 1]
    return result_list
if __name__ == '__main__':
    sample_string = "hello world"
    duplicates = find_duplicates(sample_string)
    print(duplicates)