def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1):
            is_duplicate = False
            for d_char in duplicates:
                if d_char.lower() == char.lower():
                    is_duplicate = True
                    break
            if not is_duplicate and count > 1:
                duplicates.append(char)
    return sorted(duplicates, key=str.upper)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)