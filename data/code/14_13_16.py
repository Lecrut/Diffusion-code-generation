def all_characters_distinct(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    for count in counts.values():
        if count > 1:
            return False
    
    return True

if __name__ == '__main__':
    test_string = "abcde"
    result = all_characters_distinct(test_string)
    print(result)