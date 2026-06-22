def is_all_distinct(input_string: str) -> bool:
    char_counts = dict()
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    for count in char_counts.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = is_all_distinct(test_string)
    print(result)